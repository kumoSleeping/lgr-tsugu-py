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
import base64

from tsugu import cmd_generator
from tsugu_api_core import _settings as tsugu_api_config

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

    async def _send(msg):
        msg_list = []

        # 如果是字符串，直接作为单条文本发送（避免把字符串拆成字符列表）
        if isinstance(msg, str):
            msg_list.append(Text(msg))
            # 在私聊中不使用 Quote.build，因为 FriendMessage 没有 uid 属性
            await client.send_friend_msg(msg_list, event.from_uid)
            return

        # 如果是单个 dict，包装成列表以便统一处理
        items = [msg] if isinstance(msg, dict) else msg

        for item in items:
            # 支持多种返回格式：str, bytes, 或 {'type': 'string'/'base64', 'string': ...}
            if isinstance(item, str):
                msg_list.append(Text(item))
            elif isinstance(item, (bytes, bytearray)):
                img = await client.upload_friend_image(BytesIO(item), event.from_uid)
                msg_list.append(img)
            elif isinstance(item, dict):
                t = item.get('type')
                s = item.get('string')
                if t == 'string':
                    msg_list.append(Text(s))
                elif t == 'base64' and s:
                    raw = base64.b64decode(s)
                    img = await client.upload_friend_image(BytesIO(raw), event.from_uid)
                    msg_list.append(img)
                    
        await client.send_friend_msg(msg_list, event.from_uid)

    # logger.info(f'User_{str(event.from_uin)}: {event.msg}')
    if user_blacklist:
        if str(event.from_uin) in user_blacklist:
            # logger.warning(f'User {str(event.from_uin)} is in blacklist')
            return

    await cmd_generator(message=event.msg, user_id=str(event.from_uin), send_func=_send)
    # 不发送消息


async def handle_group_message(client: Client, event: GroupMessage):
    
    async def _send(msg):
        msg_list = []

        # 如果是字符串，直接作为单条文本发送（避免把字符串拆成字符列表）
        if isinstance(msg, str):
            msg_list.append(Text(msg))
            if config_quote:
                msg_list.insert(0, Quote.build(event))
            await client.send_grp_msg(msg_list, event.grp_id)
            return

        # 如果是单个 dict，包装成列表以便统一处理
        items = [msg] if isinstance(msg, dict) else msg

        for item in items:
            # 支持多种返回格式：str, bytes, 或 {'type': 'string'/'base64', 'string': ...}
            if isinstance(item, str):
                msg_list.append(Text(item))
            elif isinstance(item, (bytes, bytearray)):
                img = await client.upload_grp_image(BytesIO(item), event.grp_id)
                msg_list.append(img)
            elif isinstance(item, dict):
                t = item.get('type')
                s = item.get('string')
                if t == 'string':
                    msg_list.append(Text(s))
                elif t == 'base64' and s:
                    raw = base64.b64decode(s)
                    img = await client.upload_grp_image(BytesIO(raw), event.grp_id)
                    msg_list.append(img)

        if config_quote:
            msg_list.insert(0, Quote.build(event))
        # logger.warning(f'send_group_message: {msg_list}')
        await client.send_grp_msg(msg_list, event.grp_id)

    if group_blacklist:
        if str(event.grp_id) in group_blacklist:
            # logger.warning(f'Group {str(event.grp_id)} is in blacklist')
            return

    await cmd_generator(message=event.msg, user_id=str(event.uin), send_func=_send)
