import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "27484828"))
API_HASH = getenv("API_HASH", "c8dc1eb163776735ed43f8d8d6ba84fd)
BOT_TOKEN = getenv("BOT_TOKEN", "6017596726:AAH5Q9KqK51JiP6m3lP0fYaxOmb_XGlbEKg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "BABZdMKdbLlB4i4x71jvnMijTaC-bb8cN98LF_QlvLQSKA0wIN8DjqdKa3o-kKY8EWvjMN4KVd_CLpVE87S_ywRjyQpgZljFPEyUa7Ssr_9WWx43BdVXRrem3lkQRQQh5k6YbWYH4_Nq3O7VX32sA3rPXObz9WUt5l_Iep6gJ66RWLv7GH4RqAq_6BedMVwcr8AcfXTzyuL5a1tERfIQoifGg17VeXRrmIACed2wIbPDZTRo73y-GK1iN15qJAzybl1673gjfElhXWgXzB1ZHnhOEMAadbhhf5RV8hYZZgjN0YTBSzdQlV287ZUb9oeLWrNneqwv5DGdrUCccB1nZNuKAAAAAXTN1dAA")
BOT_USERNAME = getenv("BOT_USERNAME", "LROBOT")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5889544325").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001946522653")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "U_Kll")
GROUP = getenv("GROUP", "U_Kll")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


