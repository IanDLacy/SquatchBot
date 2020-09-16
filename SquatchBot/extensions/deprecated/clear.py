import discord
from discord.ext import commands

class Clear(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command()
	async def clear(self,context,amount=1):
		await context.channel.purge(limit=amount)

def setup (client):
	client.add_cog(Clear(client))
