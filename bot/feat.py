from io import BytesIO
import base64
import asyncio

from lagrange.client.client import Client
from lagrange.client.events.group import GroupMessage
from lagrange.client.message.elems import At, Raw, Text

import tsugu

# 配置后端地址
# tsugu.config.backend = 'http://127.0.0.1:3000'


async def msg_handler(client: Client, event: GroupMessage):
    print(event)
    if event.msg.startswith("tsugu可爱"):
        p = await client.send_grp_msg([Text("(๑>ᴗ<๑) ")], event.grp_id)
        await asyncio.sleep(5)
        # 撤回
        await client.recall_grp_msg(event.grp_id, p)
    # elif event.msg.startswith("imgs"):
    #     await client.send_grp_msg(
    #         [
    #             await client.upload_grp_image(
    #                 open("98416427_p0.jpg", "rb"), event.grp_id
    #             )
    #         ],
    #         event.grp_id,
    #     )
    # print(f"{event.nickname}({event.grp_name}): {event.msg}")
    
    loop = asyncio.get_running_loop()
    # 默认使用 ThreadPoolExecutor，None 表示使用默认的 Executor
    result = await loop.run_in_executor(None, tsugu.bot, event.msg, event.uin, 'red', event.grp_id)
    rpl = result
    if not result:
        pass
    else:
        modified_results_grp_msg = []
        for item in rpl:
            if item['type'] == 'string':
                # 处理字符串类型的结果，可能是文本消息
                text_message = item['string']
                modified_results_grp_msg.append(Text(text_message))
            elif item['type'] == 'base64':
                # 处理Base64编码的图像数据
                base64_data = item['string']
                # 转化成bytes
                img_bytes = base64.b64decode(base64_data)
                # 上传图片
                img = await client.upload_grp_image(BytesIO(img_bytes), event.grp_id)
                modified_results_grp_msg.append(img)
                
        await client.send_grp_msg(modified_results_grp_msg, event.grp_id)
