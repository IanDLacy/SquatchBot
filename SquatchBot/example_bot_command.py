#! /usr/bin/python3

# From 'https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html'

from modules.token import token

from discord.ext import commands

bot = commands.Bot(command_prefix='./')

@bot.command()
async def test(context) :
	print('test')

bot.run(token)
