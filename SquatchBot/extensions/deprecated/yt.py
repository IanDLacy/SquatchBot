# I believe this is adapted from 'https://www.youtube.com/watch?v=MbhXIddT2YY' .
# This does not work with the newer Discord.py .

import discord
from discord.ext import commands
import youtube_dl

class YT(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command()
	async def yt(self,context,url):
		await context.voice_client.create_ytdl_player(url).start()

def setup (client):
	client.add_cog(YT(client))
