#! /usr/bin/python3

# From 'https://discordpy.readthedocs.io/en/latest/intro.html#basic-concepts'

from modules.token import token

import discord

class MyClient(discord.Client):
	async def on_ready(self):
		print(f'Logged on as {self.user}!')

	async def on_message(self, message):
		print(f'Message from {message.author}: {message.content}')

client = MyClient()

client.run(token)
