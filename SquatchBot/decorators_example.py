#! /usr/bin/python3

# From 'https://discordpy.readthedocs.io/en/latest/quickstart.html#a-minimal-bot'

from modules.token import token

import discord

client = discord.Client()

@client.event
async def on_ready():
	print(f'Logged on as {client.user}!')

@client.event
async def on_message(message):
	print(f'Message from {message.author}: {message.content}')

	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')

client.run(token)
