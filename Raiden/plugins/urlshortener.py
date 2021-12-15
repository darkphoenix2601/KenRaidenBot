from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Raiden import Raiden
from Raiden.functions import shorturl
from Raiden.utils.url import get_url
from Raiden.utils.errors import capture_err

__MODULE__ = "ᴜʀʟ ꜱʜᴏʀᴛᴇɴᴇʀ"

__HELP__ = """☆ /shorturl - Short Replyed URL\n
"""

@Raiden.on_message(filters.command("shorturl"))
@capture_err
async def shorturl(client: Client, message: Message):
  urll = get_url(message)
  url_short = shorturl.make_shorten(urll)
  await message.reply_text("Your Short URL is\n `{url_short}`")
# await message.reply_text("Usage : `/shorturl https://www.google.com`")
