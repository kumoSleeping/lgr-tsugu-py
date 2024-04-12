
# Lagrange Tsugu Python

> ✨一款 快速部署的轻量级 Tsugu 前端



## 1.⚙️准备程序

任选下方的一种方式。

### Windows exe 程序

Windows 用户可以下载 Release 中的 0.0.2-windows-amd-64.exe 文件，双击运行即可。

然后直接跳到 [2.配置文件](#2.配置文件) 继续阅读。

### Python 构建

python 版本推荐 3.10+

```shell
git clone git@github.com:kumoSleeping/lgr-tsugu-py.git
```


```shell
pip install tsugu
pip install git+https://github.com/kumoSleeping/lagrange-python
```

第一次启动：

```shell
cd lgr-tsugu-py
python bot
# python3 bot
```
会自动生成配置文件然后退出。

## 2.🖊️配置文件

使用文本编辑器打开 `config.ini` 文件，修改配置。

```ini
[DEFAULT]
lagrange_uin = 0
lagrange_sign_url = http://127.0.0.1:7140/sign
use_local_database = False
```

- `lagrange_uin`：是机器人的 QQ 号，**必须修改**。
- `lagrange_sign_url`：是 lagrange 的签名地址，**必须修改**。
- `use_local_database`：是否使用本地数据库，普通用户不建议使用。


***✨此时再次运行即可。✨***


**至此，Tsugu 已经部署完成！**


## 3.🤔常见问题

### 网络联通性问题

默认服务器后端使用 tsugubot.com 后端，主机位于日本，如果您在中国大陆使用，可能会遇到网络问题。

### 私聊

暂不支持

### 黑白名单

你直接上 QQ 把 BOT 的账号的需要关闭的群聊屏蔽了就行（

### 收不到消息 / 登陆失败

确保没有屏蔽群聊 / 免打扰 / 抢占登陆 linux QQ

### sign 填什么 

暂无，不能在公共场合泄露。


> 如有疑问可以加入 BanGDream 相关开发群 666808414 友好交流，如果您不知道什么是 BanGDream，仔细考虑您是否要加群。


## 4.📖项目依赖

### [lagrange-python](https://github.com/LagrangeDev/lagrange-python)    

~~本项目暂时依赖本人的 lagrange fork 版本，因为原项目存在问题。~~


### [tsugu-python-frontend](https://github.com/kumoSleeping/tsugu-python-frontend)   
### [tsugu-bangdream-bot](https://github.com/Yamamoto-2/tsugu-bangdream-bot)   

### 更新依赖
```shell
pip install tsugu --upgrade
pip install git+https://github.com/kumoSleeping/lagrange-python --upgrade
```

### 使用官方源安装依赖
```shell
pip install tsugu --index-url https://pypi.org/simple/
```

### 卸载依赖
```shell
pip uninstall tsugu
pip uninstall lagrange-python
```