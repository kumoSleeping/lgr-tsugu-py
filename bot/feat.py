from io import BytesIO
import os
from loguru import logger
import logging
import sys
import json

from lagrange.client.client import Client
from lagrange.client.events.group import GroupMessage
from lagrange.client.events.friend import FriendMessage
from lagrange.client.message.elems import At, Raw, Text, Quote

import tsugu
from tsugu_api_async import settings as tsugu_api_config

from config import Config


if os.path.exists('tsugu_lgr_config.json'):
    with open('tsugu_lgr_config.json', 'r') as f:
        tsugu_lgr_config_dict = json.load(f)
else:
    with open('tsugu_lgr_config.json', 'w', encoding='utf-8') as f:
        json.dump(vars(Config()), f, indent=4)
    logger.error('tsugu_lgr_config.json 不存在，请先配置 config.json')
    sys.exit(0)

# 更新配置对象
for key, value in tsugu_lgr_config_dict.items():
    if key.startswith("tsugu_api_"):
        attr_name = key.replace("tsugu_api_", "")
        if hasattr(tsugu_api_config, attr_name):
            setattr(tsugu_api_config, attr_name, value)


config_quote = tsugu_lgr_config_dict['lagrange_quote']
config_debug = tsugu_lgr_config_dict['lagrange_debug']
group_blacklist = tsugu_lgr_config_dict['lagrange_group_blacklist']
user_blacklist = tsugu_lgr_config_dict['lagrange_user_blacklist']


# 设置loguru的日志级别
logger.remove()
logger.add(sys.stdout, level="DEBUG")


def redirect_logging(record):
    logger_opt = logger.opt(depth=6, exception=record.exc_info)
    logger_opt.log(record.levelno, record.getMessage())


if config_debug:
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger().handlers = [logging.Handler()]
    logging.getLogger().handlers[0].emit = redirect_logging
else:
    logging.basicConfig(level=logging.WARNING)
    logging.getLogger().handlers = [logging.Handler()]
    logging.getLogger().handlers[0].emit = redirect_logging


async def handle_friend_message(client: Client, event: FriendMessage):
    logger.info(f'User_{str(event.from_uin)}: {event.msg}')
    if user_blacklist:
        if str(event.from_uin) in user_blacklist:
            logger.warning(f'User {str(event.from_uin)} is in blacklist')
            return

    response = await tsugu.handler_async(event.msg, str(event.from_uin), 'red', 'LgrFriend' + str(event.from_uin))
    
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
    if group_blacklist:
        if str(event.grp_id) in group_blacklist:
            logger.warning(f'Group {str(event.grp_id)} is in blacklist')
            return

    response = await tsugu.handler_async(event.msg, str(event.uin), 'red', str(event.grp_id))

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
