from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Raiden import Raiden
from Raiden.functions.shorturl import *
from Raiden.utils.url import get_url
from Raiden.utils.errors import capture_err

__MODULE__ = "ᴜʀʟ ꜱʜᴏʀᴛᴇɴᴇʀ"

__HELP__ = """☆ /shorturl - Short Replyed URL\n
"""

@Raiden.on_message(filters.command("shorturl"))
@capture_err
async def shorturl(client: Client, message: Message):
  urll = get_url(message)
  url_short = url_shortener.make_shorten(urll)
  await reply_text("Your Short URL is\n `{url_short}`")
  
