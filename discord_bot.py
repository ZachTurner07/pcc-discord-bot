import discord
import os
import re

from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("DISCORD_BOT_SECRET")

sys_admin = "zachhturner#6495"
comissioner = "jaa1221#8238"

class Bot:
   
    sys_admin = "zachhturner#6495"
    comissioner = "jaa1221#8238"

    def __init__(self, token):
        self.token = token
        self.client = discord.Client()

        @self.client.event
        async def on_ready():
            print(f'{self.client.user} has connected to Discord!')
        
        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return
            print(message.author)
            print(self.sys_admin)
            print(message.content)
            
            if message.author == self.sys_admin:
                await message.channel.send('I heard you!')
            
           # if message.author is not self.sys_admin:
           #     await message.channel.send("I'm afraid I can't do that")

    def run(self):
        self.client.run(self.token)

