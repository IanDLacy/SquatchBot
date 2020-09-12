# From 'https://discordpy.readthedocs.io/en/latest/ext/commands/extensions.html'

from discord.ext import commands

@commands.command()
async def example(context) :
	await context.send('Hello {0.display_name}.'.format(context.author))

def setup(bot) :
	bot.add_command(example)
	print('SquatchBot : Extension Setup [ example ]')

def teardown(bot) :
	print('SquatchBot : Extension Teardown [ example ]')
