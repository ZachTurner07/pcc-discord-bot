import discord
import os
import re

from dotenv import load_dotenv


import socket
import traceback

from keep_alive import keep_alive
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()
token = os.environ.get("DISCORD_BOT_SECRET")

sys_admin = "zachhturner#6495"
comissioner = "jaa1221#8238"

class Bot:

    def __init__(self, token):
        self.token = token
        self.client = discord.Client()

        @self.client.event
        async def on_ready():
            print(f'{self.client.user} has connected to Discord!')

    def run(self):
        self.client.run(self.token)

class Spreadsheet_manager:

    def __init__(self):
        self.scope = ['https://spreadsheets.google.com/feeds' + ' ' +'https://www.googleapis.com/auth/drive']
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', self.scope)
        self.gclient = gspread.authorize(self.creds)
        
        self.green_spreadsheet = self.gclient.open("Green League Match Statistics - Season 5")
        self.red_spreadsheet   = self.gclient.open("Red League Match Statistics - Season 5")
        self.blue_spreadsheet  = self.gclient.open("Blue League Match Statistics - Season 5")


#spreadsheet = gclient.open("Green League Match Statistics - Season 5")
#overall_sheet = spreadsheet.get_worksheet(0)

#team_names = overall_sheet.col_values(2)
#team_names = team_names[1:]


#client = discord.Client()

#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord!')

keep_alive()

discord_bot = Bot(token)
spreadsheet_manager = Spreadsheet_manager()

discord_bot.run()
#client.run(token)
