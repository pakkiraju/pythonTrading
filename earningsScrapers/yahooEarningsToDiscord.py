# Work with Python 3.6
from datetime import date

import discord
import pandas as pd
from discord import channel
from discord import client

TOKEN = 'xxx'

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "##er":
        pd.option_context('display.max_rows', None, 'display.max_columns', None)
        earnings = pd.read_html('https://finance.yahoo.com/calendar/earnings')[0]
        earnings.to_csv('testfile.csv') #r'earnings_{}.csv'.format(date.today()), index=None)
        await message.channel.send_file('testfile.csv')
        # await message.channel.send(earnings)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('The bot is ready!')
    game = discord.Game("##er")
    await client.change_presence(status=discord.Status.online, activity=game)


client.run(TOKEN)
