import asyncio
from lgr import main
import os
import json
from loguru import logger
import sys


if __name__ == "__main__":
    try:
        if os.path.exists('tsugu_lgr_config.json'):
            with open('tsugu_lgr_config.json', 'r') as f:
                tsugu_lgr_config_dict = json.load(f)
        else:
            logger.error('tsugu_lgr_config.json 不存在，请先配置 tsugu_lgr_config【.json')
            sys.exit(0)
        if 'lagrange_uin' not in tsugu_lgr_config_dict or tsugu_lgr_config_dict['lagrange_uin'] == '':
            logger.error('请先配置 lagrange_uin')
            sys.exit(0)
        if 'lagrange_sign_url' not in tsugu_lgr_config_dict or tsugu_lgr_config_dict['lagrange_sign_url'] == '':
            logger.error('请先配置 lagrange_sign_url')
            sys.exit(0)
        os.environ['LAGRANGE_UIN'] = tsugu_lgr_config_dict['lagrange_uin']
        os.environ['LAGRANGE_SIGN_URL'] = tsugu_lgr_config_dict['lagrange_sign_url']
        asyncio.run(main())
    except KeyboardInterrupt:
        print('\nend...')
        sys.exit(0)
