from io import BytesIO
import base64
import asyncio
import configparser
import os

from lagrange.client.client import Client
from lagrange.client.events.group import GroupMessage
from lagrange.client.events.friend import FriendMessage
from lagrange.client.message.elems import At, Raw, Text, Quote

import tsugu

if os.path.exists('config.ini'):
    config = configparser.ConfigParser()
    config.read('config.ini')
    use_local_database = config['DEFAULT']['use_local_database']
else:
    use_local_database = 'False'

if not os.path.exists('tsugu_config.json'):
    tsugu.config.output_config_json('tsugu_config.json')

if use_local_database == 'True':
    print('Using local database', use_local_database)
    tsugu.database('tsugu_database.db')
    
tsugu.config.reload_from_json('tsugu_config.json')


async def handle_friend_message(client: Client, event: FriendMessage):
    print(event)
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
    print(event)
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
        
    # 发送
    await client.send_grp_msg(text_messages + image_messages, event.grp_id)