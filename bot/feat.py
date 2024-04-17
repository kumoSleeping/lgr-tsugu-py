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

if config_debug == 'True':
    # 设置loguru的日志级别
    logger.remove()
    logger.add(sys.stdout, level="DEBUG")

    # 将logging的输出重定向到loguru
    def redirect_logging(record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


    logging.basicConfig(level=logging.DEBUG)
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
    results = await loop.run_in_executor(None, tsugu.bot, *args)
    
    # 不发送消息
    if not results:
        return
    
    # 处理所有文本类型的消息
    text_messages = [Text(item['string']) for item in results if item['type'] == 'string']
    # 异步处理所有图片类型的消息，因为 tsugu 本质不存在图文混排，因此可以并行处理
    image_messages = []
    for item in [item for item in results if item['type'] == 'base64']:
        image_message = await client.upload_friend_image(BytesIO(base64.b64decode(item['string'])), event.from_uid)
        image_messages.append(image_message)

    # 发送
    await client.send_friend_msg(text_messages + image_messages, event.from_uid)


async def handle_group_message(client: Client, event: GroupMessage):
    logger.info(f'[ {event.grp_name} ] {event.nickname}: {event.msg}')
    if Group_blacklist != {}:
        if str(event.grp_id) in Group_blacklist.values():
            logger.warning(f'Group {str(event.grp_id)} is in blacklist')
            return

    loop = asyncio.get_running_loop()
    args = (event.msg, str(event.uin), 'red', str(event.grp_id))
    results = await loop.run_in_executor(None, tsugu.bot, *args)
    
    # 不发送消息
    if not results:
        return

    # 处理所有文本类型的消息
    text_messages = [Text(item['string']) for item in results if item['type'] == 'string']
    
    # 异步处理所有图片类型的消息，因为 tsugu 本质不存在图文混排，因此可以并行处理
    image_messages = []
    for item in [item for item in results if item['type'] == 'base64']:
        image_message = await client.upload_grp_image(BytesIO(base64.b64decode(item['string'])), event.grp_id)
        image_messages.append(image_message)

    if config_quote == 'True':
        quote_message = Quote.build(event)
        text_messages.insert(0, quote_message)
        
    # 发送
    await client.send_grp_msg(text_messages + image_messages, event.grp_id)