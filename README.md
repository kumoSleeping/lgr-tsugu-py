# Lagrange Tsugu Python

> 一款有python就能用的Tsugu

## 1.安装模块
```shell
pip install tsugu
pip install git+https://github.com/kumoSleeping/lagrange-python
```

## 2.第一次启动

```shell
python bot
# python3 bot
```

## 3.配置文件

使用文本编辑器打开 `config.ini` 文件，修改配置。

```ini
[DEFAULT]
lagrange_uin = 0
lagrange_sign_url = http://127.0.0.1:7140/sign
use_local_database = False
```

- `lagrange_uin`：是机器人的 QQ 号
- `lagrange_sign_url`：是 lagrange 的签名地址
- `use_local_database`：是否使用本地数据库，如果为 `True`，则会在当前目录下生成 `database.db` 数据库文件

如有疑问可以加入 BanGDream 相关开发群 666808414 友好交流，如果您不知道什么是 BanGDream，仔细考虑您是否要加群。


## 4.再次运行

```shell
python bot
# python3 -m bot
```

## More

### 更新
```shell
pip install tsugu --upgrade
pip install git+https://github.com/kumoSleeping/lagrange-python --upgrade
```

### 使用官方源安装 tsugu
```shell
pip install tsugu --index-url https://pypi.org/simple/
```

### 卸载
```shell
pip uninstall tsugu
pip uninstall lagrange-python
```