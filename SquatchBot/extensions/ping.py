import discord
from discord.ext import commands

class Ping(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command()
	async def ping(self,context):
		await context.send(f'Pong! {round(self.client.latency*1000)}ms')

def setup (client):
	client.add_cog(Ping(client))
