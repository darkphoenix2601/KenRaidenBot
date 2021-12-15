from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from KenRaidenBot import Raiden
from Raiden.functions.shorturl import *
from Raiden.Utils.url import get_url

__MODULE__ = "ᴜʀʟ ꜱʜᴏʀᴛᴇɴᴇʀ"

__HELP__ = """☆ /shorturl - Short Replyed URL\n
"""

@Raiden.on_message(filters.command("shorturl"))
async def shorturl(client: Client, message: Message):
  urll = get_url(message)
  url_short = url_shortener.make_shorten(urll)
  await reply_text("Your Short URL is\n `{url_short}`")
  
