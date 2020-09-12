#! /usr/bin/python3

# From 'https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html'

from modules.token import token

from discord.ext import commands

@commands.command()
async def test(context) :
	print('test')

bot = commands.Bot(command_prefix='./')

bot.add_command(test)

bot.run(token)
