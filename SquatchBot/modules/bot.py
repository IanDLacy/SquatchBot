from modules.token import token

print ( '\nSquatchBot : Starting' )

from discord.ext import commands

commands.DefaultHelpCommand.get_ending_note = lambda self : \
	f'Run `{self.clean_prefix}{self.invoked_with} [ Category | Command ]` for specifics.\n'

bot = commands.Bot	(

			command_prefix = commands.when_mentioned_or	(

									'sb> ' , 'Sb> ' , 'SB> ' ,
									'sb>'  , 'Sb>'  , 'SB>'  ,

									'sb://' , 'Sb://' , 'SB://' ,

									'sb: ' , 'Sb: ' , 'SB: ' ,
									'sb:'  , 'Sb:'  , 'SB:'  ,

									'sb$ ' , 'Sb$ ' , 'SB$ ' ,
									'sb$'  , 'Sb$'  , 'SB$'  ,

									'sb# ' , 'Sb# ' , 'SB# ' ,
									'sb#'  , 'Sb#'  , 'SB#'  ,

									'sb.' , 'Sb.' , 'SB.' ,
									'sb/' , 'Sb/' , 'SB/' ,
									'sb?' , 'Sb?' , 'SB?' ,

									'sb ' , 'Sb ' , 'SB ' ,
									'sb'  , 'Sb'  , 'SB'  ,

									'squatchbot ' , 'Squatchbot ' , 'SquatchBot ' , 'SQUATCHBOT '

									) ,
			case_insensitive = True ,
			description = 'SquatchBot!' ,
			self_bot = False ,
			help_command = commands.DefaultHelpCommand	(

									width = 128 ,
									sort_commands = True ,
									dm_help = False ,
									dm_help_threshold = 1000 ,
									indent = 2 ,
									commands_heading = 'Commands:' ,
									command_attrs =	{

											'name' : 'Help' ,
											'brief' : 'SquatchBot Help' ,
											'description' : 'SquatchBot Help' ,
											'aliases' :	[

													'?'      ,
													'-h'     ,
													'--help' ,
													'h'

													] ,
											'usage' : '[ Category | Command ]' ,
											'help' : 'Running this command displays various help information.'

											} ,
									no_category = 'Miscellaneous' ,
									paginator = commands.Paginator	(

													prefix = '```fix' ,
													suffix = '```' ,
													max_size = 2000

													)

									) ,

			)

import os

for file in os.listdir( './SquatchBot/extensions/commands/' ) :
	if file.endswith('.py') :
		bot.load_extension(f'extensions.commands.{file[:-3]}')

for file in os.listdir( './SquatchBot/extensions/cogs/' ) :
	if file.endswith('.py') :
		bot.load_extension(f'extensions.cogs.{file[:-3]}')

@bot.event
async def on_ready():
	print('\nSquatchBot : Ready')

bot.run(token)
