from typing import List, Union, Optional


class Config:
    def __init__(self):
        self.lagrange_uin: str = ''
        """
        **必填**
        lagrange_uin 登录账号
        """

        self.lagrange_sign_url: str = ''
        """
        **必填**
        lagrange_sign_url 签名地址
        """

        self.lagrange_group_blacklist: List[str] = []
        """
        lagrange_group_blacklist 群黑名单
        例: ["123456789", "987654321"]
        """

        self.lagrange_user_blacklist: List[str] = []
        """
        lagrange_user_blacklist 用户黑名单
        例: ["123456789", "987654321"]
        """

        self.lagrange_debug: bool = True
        """
        lagrange_debug 是否开启调试模式日志
        """

        self.lagrange_quote: bool = False
        """
        lagrange_quote 是否开启引用回复
        """

        self.tsugu_api_timeout: int = 10
        '''
        请求超时时间
        '''

        self.tsugu_api_proxy: str = ''
        '''
        代理地址
        '''

        self.tsugu_api_backend_url: str = 'http://tsugubot.com:8080'
        '''
        后端地址
        默认为 Tsugu 官方后端，若有自建后端服务器可进行修改。
        '''

        self.tsugu_api_backend_proxy: bool = True
        '''
        是否使用后端代理
        当设置代理地址后可修改此项以决定是否使用代理。
        默认为 True，即使用后端代理。若使用代理时后端服务器无法访问，可将此项设置为 False。
        '''

        self.tsugu_api_userdata_backend_url: str = 'http://tsugubot.com:8080'
        '''
        用户数据后端地址
        默认为 Tsugu 官方后端，若有自建后端服务器可进行修改。
        '''

        self.tsugu_api_userdata_backend_proxy: bool = True
        '''
        是否使用用户数据后端代理
        当设置代理地址后可修改此项以决定是否使用代理。
        默认为 True，即使用后端代理。若使用代理时后端服务器无法访问，可将此项设置为 False。
        '''

        self.tsugu_api_use_easy_bg: bool = True
        '''
        是否使用简易背景，使用可在降低背景质量的前提下加快响应速度。
        默认为 True，即使用简易背景。若不使用简易背景，可将此项设置为 False。
        '''

        self.tsugu_api_compress: bool = True
        '''
        是否压缩返回数据，压缩可减少返回数据大小。
        默认为 True，即压缩返回数据。若不压缩返回数据，可将此项设置为 False。
        '''

        self.tsugu_compact: bool = True
        '''
        是否允许命令与参数之间没有空格
        '''

        self.tsugu_disable_gacha_simulate_group_ids: List = []
        '''
        需要关闭模拟抽卡的群
        '''