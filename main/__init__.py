#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "22238137" #config("API_ID", default=None, cast=int)
API_HASH = "538dbae7aa6feae4b5a83f54cb8268a6" #config("API_HASH", default=None)
BOT_TOKEN = "7688529622:AAHxvPDvJVgcRYO_FvimKY4QCpeOvL1kX8Y" #config("BOT_TOKEN", default=None)
SESSION = "BQFTU7kAikxiSRGWMM9ZAVGYES6Jr8-NYuqQxa34zR5NJoTAl1h3wA50K9Bn2PZL2QeLUpdnrDbbIiTcng7RTPal8vPnON5Lxw1ezIGQj7Qzz6Po3OujoFW1dbCly6mQQzGUnCOYEnxRiSXquK4bOwcXqVLNKjJEIcADv25bwEoX4A6-lFRL_rEp_OmzO3g5gPswcw2buWtdL-99FKF07TZrWE6wNV9sK6g3aAWbh27icOMBGYUw2LUNpY3324qV_yazLJGhRk_uzI3wWQ4eBKP9_eD1y4D2F7cXSTms2b4xbOFteX24DxW3NlzBXOoxgeVx0LH-2r72mD6MaF_NB6j9Iuw6rQAAAAGpdkUbAA" #config("SESSION", default=None)
FORCESUB = "noforwreskoo" #config("FORCESUB", default=None)
AUTH = "7138067739" #config("AUTH", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
