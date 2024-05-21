
<h1 align="center"> Lagrange Tsugu Python 
<img src="./logo.jpg" width="100" height="100" alt="nina"/> 
</h1>



## 💻 准备程序

任选下方的一种方式即可。

- **Windows exe 程序 💻**   
    Windows 用户可以下载 Release 中的 tsugu-Windows-amd64-1.x.x.exe 文件，双击运行即可。   
    然后直接跳到 `📱📷 登陆` 继续阅读。


- **Python 构建 🐍**
    ```shell
    # 已安装 git
    git clone git@github.com:kumoSleeping/lgr-tsugu-py.git

    # python 版本推荐 3.10+
    pip install tsugu
    pip install git+https://github.com/LagrangeDev/lagrange-python@broken

    cd lgr-tsugu-py
    python bot
    # python3 bot
    ```

## 📱📷 登陆

完成上面的操作后会生成配置文件，使用文本编辑器打开 `tsugu_lgr_config.json` 文件，修改配置。

- lagrange_uin
- lagrange_sign_url

上方两个配置项必填，其他配置项可根据需求修改。 
然后运行项目，同目录下会生成二维码图片，打开后使用 BOT 账号扫码登陆即可。


## 📒🖊️⌨️ 配置

```py
lagrange_uin: str = ''
"""
**必填**
lagrange_uin 登录账号
"""

lagrange_sign_url: str = ''
"""
**必填**
lagrange_sign_url 签名地址
"""

lagrange_group_blacklist: List[str] = []
"""
lagrange_group_blacklist 群黑名单
例: ["123456789", "987654321"]
"""

lagrange_user_blacklist: List[str] = []
"""
lagrange_user_blacklist 用户黑名单
例: ["123456789", "987654321"]
"""

lagrange_debug: bool = True
"""
lagrange_debug 是否开启调试模式日志
"""

lagrange_quote: bool = False
"""
lagrange_quote 是否开启引用回复
"""

tsugu_compact = True
'''
是否允许命令与参数之间没有空格
'''

tsugu_disable_gacha_simulate_group_ids = []
'''
需要关闭模拟抽卡的群
'''

tsugu_api_timeout: int = 10
'''
请求超时时间
'''

tsugu_api_proxy: str = ''
'''
代理地址
'''

tsugu_api_backend_url: str = 'http://tsugubot.com:8080'
'''
后端地址
默认为 Tsugu 官方后端，若有自建后端服务器可进行修改。
'''

tsugu_api_backend_proxy: bool = True
'''
是否使用后端代理
当设置代理地址后可修改此项以决定是否使用代理。
默认为 True，即使用后端代理。若使用代理时后端服务器无法访问，可将此项设置为 False。
'''

tsugu_api_userdata_backend_url: str = 'http://tsugubot.com:8080'
'''
用户数据后端地址
默认为 Tsugu 官方后端，若有自建后端服务器可进行修改。
'''

tsugu_api_userdata_backend_proxy: bool = True
'''
是否使用用户数据后端代理
当设置代理地址后可修改此项以决定是否使用代理。
默认为 True，即使用后端代理。若使用代理时后端服务器无法访问，可将此项设置为 False。
'''

tsugu_api_use_easy_bg: bool = True
'''
是否使用简易背景，使用可在降低背景质量的前提下加快响应速度。
默认为 True，即使用简易背景。若不使用简易背景，可将此项设置为 False。
'''

tsugu_api_compress: bool = True
'''
是否压缩返回数据，压缩可减少返回数据大小。
默认为 True，即压缩返回数据。若不压缩返回数据，可将此项设置为 False。
'''
```

**此时运行项目，同目录下会生成二维码图片，打开后使用 BOT 账号扫码登陆即可。**

## 🤔 常见问题


[//]: # (表格)

| 问题           | 解决方案                                           |
|--------------|------------------------------------------------|
| 网络联通性问题      | 启用代理 / 更换后端或自建后端                               |
| 收不到消息 / 登陆失败 | 确保没有屏蔽群聊 / 免打扰 / 抢占登陆 linux QQ / 正确配置 sign 地址。 |
| sign 填什么     | 不能在公共场合泄露。                                     |


> 如有疑问可以加入 BanGDream 相关开发群 666808414 友好交流，如果您不知道什么是 BanGDream，仔细考虑您是否要加群。


## 📖 项目依赖

| 项目 | 说明 | 技术栈 |
| --- | --- | --- |
[lagrange-python](https://github.com/LagrangeDev/lagrange-python)  | BOT 登陆端 | Python / Lagrange.core |
[tsugu-python-frontend](https://github.com/kumoSleeping/tsugu-python-frontend)    | Tsugu 前端 | Python |
[tsugu-bangdream-bot](https://github.com/Yamamoto-2/tsugu-bangdream-bot)    | Tsugu 后端 | Node.js |

- 更新依赖 ⬆
    ```shell
    pip install tsugu --upgrade

    pip uninstall lagrange-python
    pip install git+https://github.com/LagrangeDev/lagrange-python@broken
    ```

- 卸载依赖 🗑
    ```shell
    pip uninstall tsugu
    pip uninstall lagrange-python
    ```

## 📦 版本更新

> 如果您是 exe 用户，无需关注*号内容

| 版本     | 更新内容                   | 配置文件增删                                  | *需要 git pull 本项目 | *建议更新 lagrange | *需要更新 tsugu 至 |
|--------|------------------------|-----------------------------------------|------------------|----------------|---------------|
| 1.1.0  | 兼容新版chat tsugu         | 少了点配置                                   | ✓                | -              | 1.1.0         |
| 1.0.1  | 修复exit，改变配置文件命名        | 改变配置文件命名                                | ✓                | -              | 1.0.6         |
| 1.0.0  | 进入一个正式版本               | 完全改变                                    | ✓                | ✓              | 1.0.6         |
| 0.0.14 | 修复help无响应              | -                                       | -                | -              | 0.5.7         |
| 0.0.13 | 修复bug若干                | -                                       | -                | -              | -             |
| 0.0.12 | 修复bug若干                | -                                       | -                | -              | 0.5.4         |
| 0.0.11 | 更换 log 支持黑名单 支持开关debug | config.ini 更新                           | ✓                | -              | 0.4.14        |
| 0.0.10 | 修复本地数据库启用失败 bug、细节优化   | -                                       | ✓                | -              | 0.4.11        |
| 0.0.9  | tsugu 更换网络库为 urllib3   | tsugu_config.json 更新                    | -                | -              | 0.4.10        |
| 0.0.8  | 网络相关 log 优化            | -                                       | -                | -              | 0.4.7         |
| 0.0.7  | -                      | -                                       | -                | -              | -             |
| 0.0.6  | 支持help                 | tsugu_config.json 更新                    | -                | -              | 0.4.6         |
| 0.0.5  | -                      | -                                       | -                | -              | 0.3.6         |
| 0.0.4  | -                      | -                                       | -                | -              | 0.3.5         |
| 0.0.3  | 支持私聊、引用回复、优化细节         | config.ini 增加 quote = False             | ✓                | ✓              | -             |
| 0.0.2  | 支持本地数据库                | config.ini 增加 use_local_database = True | ✓                | -              | 0.3.4         |
| 0.0.1  | -                      | -                                       | -                | -              | -             |
