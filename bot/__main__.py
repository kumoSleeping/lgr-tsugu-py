import os
import asyncio
from lgr import main


if __name__ == "__main__":
    import configparser
    # 检测 config.ini 是否存在
    if not os.path.exists('config.ini'):
        print('config.ini 不存在，请先配置 config.ini')
        
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'LAGRANGE_UIN': '0', 'LAGRANGE_SIGN_URL': 'http://127.0.0.1:7140/sign', 'use_local_database': 'False', 'quote': 'False', 'debug': 'True'}
        config['GroupBlacklist'] = {'Group1': '123456789', 'Group2': '987654321'}
        config['UserBlacklist'] = {'User1': '1145141919810'}
        with open('config.ini', 'w') as f:
            config.write(f)
        exit(0)
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    os.environ['LAGRANGE_UIN'] = config['DEFAULT']['LAGRANGE_UIN']
    os.environ['LAGRANGE_SIGN_URL'] = config['DEFAULT']['LAGRANGE_SIGN_URL']
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nend...')
        exit(0)
