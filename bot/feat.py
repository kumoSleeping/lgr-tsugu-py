from io import BytesIO
import base64
import asyncio
import configparser
import os
from loguru import logger
import logging
import sys

from lagrange.client.client import Client
from lagrange.client.events.group import GroupMessage
from lagrange.client.events.friend import FriendMessage
from lagrange.client.message.elems import At, Raw, Text, Quote

import tsugu


if os.path.exists('config.ini'):
    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        use_local_database = config['DEFAULT']['use_local_database']
    except KeyError:
        use_local_database = 'False'
    try:
        config_quote = config['DEFAULT']['quote']
    except KeyError:
        config_quote = 'False'
    try:
        config_debug = config['DEFAULT']['debug']
    except KeyError:
        config_debug = 'True'
    try:
        Group_blacklist = config['GroupBlacklist']
    except KeyError:
        Group_blacklist = {}
    try:
        User_blacklist = config['UserBlacklist']
    except KeyError:
        User_blacklist = {}
else:
    use_local_database = 'False'
    config_quote = 'False'
    config_debug = 'True'
    Group_blacklist = {}
    User_blacklist = {}


if not os.path.exists('tsugu_config.json'):
    tsugu.config.output_config_json('tsugu_config.json')

    
tsugu.config.reload_from_json('tsugu_config.json')
# 设置loguru的日志级别
logger.remove()
logger.add(sys.stdout, level="DEBUG")


# 将logging的输出重定向到loguru
def redirect_logging(record):
    logger_opt = logger.opt(depth=6, exception=record.exc_info)
    logger_opt.log(record.levelno, record.getMessage())


if config_debug == 'True':
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger().handlers = [logging.Handler()]
    logging.getLogger().handlers[0].emit = redirect_logging
else:
    logging.basicConfig(level=logging.WARNING)
    logging.getLogger().handlers = [logging.Handler()]
    logging.getLogger().handlers[0].emit = redirect_logging


if use_local_database == 'True':
    logger.info(f'Using local tsugu player data database.')
    tsugu.database('tsugu_database.db')


async def handle_friend_message(client: Client, event: FriendMessage):
    logger.info(f'User_{str(event.from_uin)}: {event.msg}')
    if User_blacklist != {}:
        if str(event.from_uin) in User_blacklist.values():
            logger.warning(f'User {str(event.from_uin)} is in blacklist')
            return

    loop = asyncio.get_running_loop()
    args = (event.msg, str(event.from_uin), 'red', 'LgrFriend' + str(event.from_uin))
    response = await loop.run_in_executor(None, tsugu.handler, *args)
    
    # 不发送消息
    if not response:
        return

    msg_list = []
    for item in response:
        # 处理文本类型的消息
        msg_list.append(Text(item)) if isinstance(item, str) else None
        msg_list.append(await client.upload_friend_image(BytesIO(item), event.from_uid)) if isinstance(item, bytes) else None

    await client.send_friend_msg(msg_list, event.from_uid)


async def handle_group_message(client: Client, event: GroupMessage):
    logger.info(f'[ {event.grp_name} ] {event.nickname}: {event.msg}')
    if Group_blacklist != {}:
        if str(event.grp_id) in Group_blacklist.values():
            logger.warning(f'Group {str(event.grp_id)} is in blacklist')
            return

    loop = asyncio.get_running_loop()
    args = (event.msg, str(event.uin), 'red', str(event.grp_id))
    response = await loop.run_in_executor(None, tsugu.handler, *args)

    # 不发送消息
    if not response:
        return

    msg_list = []
    for item in response:
        # 处理文本类型的消息
        msg_list.append(Text(item)) if isinstance(item, str) else None
        msg_list.append(await client.upload_grp_image(BytesIO(item), event.grp_id)) if isinstance(item, bytes) else None

    if config_quote == 'True':
        msg_list.insert(0, Quote.build(event))

    await client.send_grp_msg(msg_list, event.grp_id)
