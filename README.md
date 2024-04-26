
<h1 align="center"> Lagrange Tsugu Python 
<img src="./logo.jpg" width="100" height="100" alt="nina"/> 
</h1>



## ⚙️ 准备程序

任选下方的一种方式即可。

- **Windows exe 程序 💻**   
    Windows 用户可以下载 Release 中的 tsugu-Windows-amd64-0.x.x.exe 文件，双击运行即可。   
    然后直接跳到 `🖊️ 配置登陆` 继续阅读。


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

## 🖊️ 配置登陆

完成上面的操作后会生成配置文件，使用文本编辑器打开 `config.ini` 文件，修改配置。

```ini
[DEFAULT]
lagrange_uin = 0
lagrange_sign_url = http://127.0.0.1:7140/sign
use_local_database = False
quote = False
debug = True

[GroupBlacklist]
Group1 = 123456789
Group2 = 987654321

[UserBlacklist]
User1 = 123456789
```

- `lagrange_uin`：是机器人的 QQ 号，**必须修改**。
- `lagrange_sign_url`：是 lagrange 的签名地址，**必须修改**。
- `use_local_database`：是否使用本地数据库，普通用户不建议使用。
- `quote`：是否开启引用回复。
- `debug`：是否开启 debug 模式。
- `GroupBlacklist`：群聊黑名单，**可选**。
- `UserBlacklist`：用户黑名单，**可选**。

**此时运行项目，同目录下会生成二维码图片，打开后使用 BOT 账号扫码登陆即可。**

## 🤔 常见问题


[//]: # (表格)

| 问题           | 解决方案                                           |
|--------------|------------------------------------------------|
| 网络联通性问题      | 启用代理 / 更换后端或自建后端 / config.ini 启动本地数据库          |
| 网络代理问题         | 当你本地启动好代理时，更改 tsugu_config.json 配置             |
| 收不到消息 / 登陆失败 | 确保没有屏蔽群聊 / 免打扰 / 抢占登陆 linux QQ / 正确配置 sign 地址。 |
| sign 填什么     | 暂无，不能在公共场合泄露。                                  |


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

| 版本     | 更新内容                 | 配置文件增删                                  | *需要 git pull 本项目 | *建议更新 lagrange | *需要更新 tsugu 至 |
|--------|----------------------|-----------------------------------------|------------------|---------------|---------------|
| 0.0.13 | 修复bug若干          |                           | -                | - | -             |
| 0.0.12 | 修复bug若干              |                           | -                | - | 0.5.4         |
| 0.0.11 | 更换 log 支持黑名单 支持开关debug | config.ini 更新                                     | ✓                | - | 0.4.14        |
| 0.0.10 | 修复本地数据库启用失败 bug、细节优化 | -                                       | ✓                | - | 0.4.11        |
| 0.0.9  | tsugu 更换网络库为 urllib3 | tsugu_config.json 更新                    | -                | - | 0.4.10        |
| 0.0.8  | 网络相关 log 优化          | -                                       | -                | - | 0.4.7         |
| 0.0.7  | -                    | -                                       | -                | - | -             |
| 0.0.6  | 支持help               | tsugu_config.json 更新                    | -                | - | 0.4.6         |
| 0.0.5  | -                    | -                                       | -                | - | 0.3.6         |
| 0.0.4  | -                    | -                                       | -                | - | 0.3.5         |
| 0.0.3  | 支持私聊、引用回复、优化细节       | config.ini 增加 quote = False             | ✓                | ✓ | -             |
| 0.0.2  | 支持本地数据库              | config.ini 增加 use_local_database = True | ✓                | - | 0.3.4         |
| 0.0.1  | -                    | -                                       | -                | - | -             |
