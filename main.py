import discord
import os
import re

from dotenv import load_dotenv


import socket
import traceback

from keep_alive import keep_alive
from spreadsheet_manager import Spreadsheet_manager
from discord_bot import Bot

load_dotenv()
token = os.environ.get("DISCORD_BOT_SECRET")

def main():
    keep_alive()

    discord_bot = Bot(token)
    spreadsheet_manager = Spreadsheet_manager()

    discord_bot.run()


if __name__ == "__main__":
    main()
