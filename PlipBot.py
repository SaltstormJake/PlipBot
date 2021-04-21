import discord
from discord.ext import commands
import config
token = config.token

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    sentence = message.content.lower()
    if 'clim' in sentence:
        await message.channel.send('HEE HEE HEE HEEEEEUUUUE')
    if 'plip' in sentence:
        await message.channel.send('Plip!')
    elif 'disgaea' in sentence:
        await message.channel.send('Plip!')
    elif 'ace combat' in sentence:
        await message.channel.send('Plip!')
    elif 'cheese' in sentence:
        await message.channel.send('Plip!')

client.run(token)
    