# Work with Python 3.6
import discord
import pandas as pd
from discord import channel
from discord import client

TOKEN = 'NjQ1OTAxNjE0MTQ5Nzk1ODQw.XdJsVQ.CVXfWwlCCVZtWoidjKv_5rKDtJs'

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "##er":
        pd.option_context('display.max_rows', True, 'display.max_columns', True)
        earnings = pd.read_html('https://finance.yahoo.com/calendar/earnings')[0]
        await message.channel.send(earnings)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('The bot is ready!')
    game = discord.Game("with the API")
    await client.change_presence(status=discord.Status.online, activity=game)


client.run(TOKEN)
