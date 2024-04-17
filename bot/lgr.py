import asyncio
from loguru import logger
import os

from lagrange.client.client import Client
from lagrange.client.events.group import GroupMessage
from lagrange.client.events.friend import FriendMessage
from lagrange.client.events.service import ServerKick
from lagrange.client.message.elems import At, Raw, Text
from lagrange.info.app import app_list
from lagrange.info.device import DeviceInfo
from lagrange.info.sig import SigInfo
from lagrange.utils.sign import sign_provider

from feat import handle_friend_message, handle_group_message

DEVICE_INFO_PATH = "./device.json"
SIGINFO_PATH = "./sig.bin"


class InfoManager:
    def __init__(self, uin: int, device_info_path: str, sig_info_path: str):
        self.uin: int = uin
        self._device_info_path: str = device_info_path
        self._sig_info_path: str = sig_info_path
        self._device = None
        self._sig_info = None

    @property
    def device(self) -> DeviceInfo:
        assert self._device, "Device not initialized"
        return self._device

    @property
    def sig_info(self) -> SigInfo:
        assert self._sig_info, "SigInfo not initialized"
        return self._sig_info

    def save_all(self):
        with open(self._sig_info_path, "wb") as f:
            f.write(self._sig_info.dump())

        with open(self._device_info_path, "wb") as f:
            f.write(self._device.dump())

        logger.success("device info saved")

    def __enter__(self):
        if os.path.isfile(self._device_info_path):
            with open(self._device_info_path, "rb") as f:
                self._device = DeviceInfo.load(f.read())
        else:
            logger.error(f"{self._device_info_path} not found, generating...")
            self._device = DeviceInfo.generate(self.uin)

        if os.path.isfile(self._sig_info_path):
            with open(self._sig_info_path, "rb") as f:
                self._sig_info = SigInfo.load(f.read())
        else:
            logger.warning(f"{self._sig_info_path} not found, generating...")
            self._sig_info = SigInfo.new(8848)
        return self

    def __exit__(self, *_):
        pass


async def heartbeat_task(client: Client):
    while True:
        await client.online.wait()
        await asyncio.sleep(120)
        logger.info(f"{round(await client.sso_heartbeat(True) * 1000, 2)}ms to server")


async def handle_kick(client: "Client", event: "ServerKick"):
    logger.error(f"被服务器踢出：[{event.title}] {event.tips}")
    await client.stop()


async def main():
    uin = int(os.environ.get("LAGRANGE_UIN", "0"))
    sign_url = os.environ.get("LAGRANGE_SIGN_URL", "")

    app = app_list["linux"]

    with InfoManager(uin, DEVICE_INFO_PATH, SIGINFO_PATH) as im:
        client = Client(
            uin,
            app,
            im.device,
            im.sig_info,
            sign_provider(sign_url) if sign_url else None,
        )
        # client.events.subscribe(GroupMessage, receive_message_miao)  # 注册接收消息的函数
        client.events.subscribe(GroupMessage, handle_group_message)
        client.events.subscribe(ServerKick, handle_kick)
        client.events.subscribe(FriendMessage, handle_friend_message)
        
        client.connect()
        asyncio.create_task(heartbeat_task(client))
        if im.sig_info.d2:
            if not await client.register():
                await client.login()
        else:
            await client.login()
        im.save_all()
        await client.wait_closed()

