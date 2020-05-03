import json
import logging
import sys
from os.path import dirname

PARENT_DIR = '/'.join(dirname(__file__).split('/')[:-1])

# read bog config
with open(f'{PARENT_DIR}/config.json', 'r') as f:
    CONFIG = json.load(f)
API_KEY = CONFIG['api_key']
API_HASH = CONFIG['api_hash']
BOT_TOKEN = CONFIG['tg_bot_token']
BOT_ID = CONFIG['tg_bot_id']
CURRENCY_API = CONFIG['currency_api']

# set logging
FORMATTER = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s'
                              '[%(module)s.%(funcName)s:%(lineno)d]: %(message)s')
OUT = logging.StreamHandler(sys.stdout)
ERR = logging.StreamHandler(sys.stderr)
OUT.setFormatter(FORMATTER)
ERR.setFormatter(FORMATTER)
OUT.setLevel(logging.INFO)
ERR.setLevel(logging.WARNING)
LOGGER = logging.getLogger()
LOGGER.addHandler(OUT)
LOGGER.addHandler(ERR)
LOGGER.setLevel(logging.INFO)
