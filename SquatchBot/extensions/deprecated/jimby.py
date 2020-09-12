# Boilerplate Cog|Extension Adapted From 'https://youtu.be/vQw8cFfZPx0'

import discord
from discord.ext import commands

class Jimby(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command()
	async def jimby(self,context):
		await context.send('Hi Jimby!')

def setup (client):
	client.add_cog(Jimby(client))
