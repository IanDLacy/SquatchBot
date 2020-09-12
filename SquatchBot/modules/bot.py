from modules.token import token

print ('\nSquatchBot : Starting')

import discord
from discord.ext import commands

import os

client = commands.Bot( command_prefix = './' )

for file in os.listdir( './SquatchBot/extensions' ) :
	if file.endswith('.py') :
		client.load_extension(f'extensions.{file[:-3]}')
@client.event
async def on_ready():
	print('\nSquatchBot : Ready')

client.run(token)
