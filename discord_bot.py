import sys
from random import choice
import os
import discord





# Discord Bot Set Up
client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # If the user says hello, say hello back
    if message.content.startswith('$hello'):
        await message.channel.send('Hello there!')
    
    # If the user asks for wisdom, generate a random piece of wisdom
    elif message.content.startswith('$wisdom?'):
        await message.channel.send('you must complete your training before receiving this wisdom...check back later')

# Run the Discord Bot
client.run(os.environ['DISCORD_TOKEN'])