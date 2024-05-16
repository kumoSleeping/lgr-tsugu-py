import asyncio
from lgr import main
import os
import json
from loguru import logger
from config import Config


if __name__ == "__main__":
    try:
        if os.path.exists('config.json'):
            with open('config.json', 'r') as f:
                tsugu_lgr_config_dict = json.load(f)
        else:
            logger.error('config.json 不存在，请先配置 config.json')
            exit(0)
        if 'lagrange_uin' not in tsugu_lgr_config_dict or tsugu_lgr_config_dict['lagrange_uin'] == '':
            logger.error('请先配置 lagrange_uin')
            exit(0)
        if 'lagrange_sign_url' not in tsugu_lgr_config_dict or tsugu_lgr_config_dict['lagrange_sign_url'] == '':
            logger.error('请先配置 lagrange_sign_url')
            exit(0)
        os.environ['LAGRANGE_UIN'] = tsugu_lgr_config_dict['lagrange_uin']
        os.environ['LAGRANGE_SIGN_URL'] = tsugu_lgr_config_dict['lagrange_sign_url']
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nend...')
        exit(0)
