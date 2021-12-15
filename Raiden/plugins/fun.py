import random
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Raiden import Raiden
from Raiden.utils.errors import capture_err 
__MODULE__ = "Fun" 
__HELP__ = """☆ /toss - Toss """

@Raiden.on_message(filters.command("toss"))
async def toss(client: Client, message: Message):
  tossed = random.choice(["Heads", "Tails"])
  message.reply("Here Comes {tossed}!")
