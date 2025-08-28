
<h1 align="center"> Lagrange Tsugu Python 
<img src="./logo.jpg" width="50" height="50" alt="nina"/> 
</h1>



## 📦 快速开始

目前支持 macOS_Arm64, Windows_amd64, Linux_amd64 三种主流平台的预编译版本，其他平台请使用 Python 构建方式。
下载 Release 中的 对应的版本 , 给予足够的权限后运行, 跟随下方 "扫码登陆" 部分指引完成部署.

## 📱 扫码登陆

完成上面的操作后会生成配置文件，使用文本编辑器打开 `tsugu_lgr_config.json` 文件，修改配置。

- lagrange_uin :QQ号
- lagrange_sign_url :sign地址

上方两个配置项必填，其他配置项可根据需求修改。 
然后运行项目，同目录下会生成二维码图片，打开后使用 BOT 账号扫码登陆即可。

## 🤔 常见问题


[//]: # (表格)

| 问题           | 解决方案                                           |
|--------------|------------------------------------------------|
| 网络联通性问题      | 启用代理 / 更换后端或自建后端                               |
| 收不到消息 / 登陆失败 | 确保没有屏蔽群聊 / 免打扰 / 抢占登陆 linux QQ / 正确配置 sign 地址。 |
| sign 填什么     | 可以在lagrange相关社群或其他BOT开发相关社群询问                      |


> 如有疑问可以加入 BanG Dream Bot 相关开发群 666808414 友好交流，如果您不知道什么是 BanGDream，仔细考虑您是否要加群。

## 从 Python 构建 
    ```shell
    # 已安装 git
    git clone git@github.com:kumoSleeping/lgr-tsugu-py.git
    pip install tsugu
    pip install git+https://github.com/LagrangeDev/lagrange-python@broken

    cd lgr-tsugu-py
    python bot
    # python3 bot
    ```
    > 如果未安装git也可以使用下载本项目和 lagrange-python 的 zip 包的方式构建, 但长期使用更新较为麻烦。

## 📖 项目依赖

- [lagrange-python](https://github.com/LagrangeDev/lagrange-python)  
- [tsugu-b3](https://github.com/kumoSleeping/tsugu-b3)  
- [tsugu-bangdream-bot](https://github.com/Yamamoto-2/tsugu-bangdream-bot)  

### 更新依赖
    ```shell
    pip install tsugu --upgrade

    pip uninstall lagrange-python
    pip install git+https://github.com/LagrangeDev/lagrange-python@broken
    ```

### 卸载依赖
    ```shell
    pip uninstall tsugu
    pip uninstall lagrange-python
    ```

## 版本更新日志

> 如果您是 exe 用户，无需关注*号内容

| 版本     | 更新内容                   | 配置文件增删                     | *需要 git pull 本项目 | *建议更新 lagrange | *需要更新 tsugu-b3 至 |
|--------|------------------------|-----------------------------------------|------------------|----------------|---------------|
| 2.2.3  | -                | -                                         | -                |    -          | 6.3.2         |
| 2.0.1  | -                | -                                         | -                |    -          | 6.2.3         |
| 2.0.0  | 全盘更新                | 全盘更新                              | ✓                |    ✓          | 6.2.2         |
| 1.2.2  | -                      | -                                       | -                | -              | 2.0.3         |
| 1.2.1  | -                      | -                                       | -                | -              | 2.0.2         |
| 1.2.0  | 兼容 2.0.0 chat tsugu    | 配置文件改变                                  | ✓                | -              | 2.0.1         |
| 1.1.0  | 兼容新版chat tsugu         |                                         | ✓                | -              | 1.1.0         |
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
