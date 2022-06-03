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
        random_wisdom = choice(open("wisdom.txt").readlines())
        await message.channel.send(random_wisdom)

    elif message.content.startswith('$prequel'):
        random_prequel_quote = choice(open("prequel_quotes.txt").readlines())
        await message.channel.send(random_prequel_quote)
    
    elif message.content.startswith('%hello there'):
        await message.channel.send("General Kenobi. You are a bold one.")
    
    elif message.content.startswith('%your move'):
        await message.channel.send("You fool. I've been trained in your Jedi arts by Count Dooku.")
    
    elif message.content.startswith('%lightsaber activate'):
        await message.channel.send("wwwwOOWWwww...WOOOOwwwwwwwOOOWwwww ... BJJJJJJJZZZZHKKHKJZJJJJJJJZZZZZZZvvvwwommmmm")

# Run the Discord Bot
client.run(os.environ['DISCORD_TOKEN'])