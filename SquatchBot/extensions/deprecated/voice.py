# I believe this is scraped from 'examples/basic_voice.py' ?
# This might also have been adapted from 'https://www.youtube.com/watch?v=hFVby_Vet7E' .
# Maybe both ?
# I believe this works though .

import discord
from discord.ext import commands

class Voice(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command()
	async def voice(self,context,action='invalid'):
		if action == 'join':
			await context.author.voice.channel.connect()
		elif action == 'leave':
			await context.voice_client.disconnect()
		else:
			await context.send('Invalid Command Syntax')

def setup (client):
	client.add_cog(Voice(client))
