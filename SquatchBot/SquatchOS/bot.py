import SquatchOS
from discord.ext import commands

def configure (  ) :

	print ( '\nSquatchOS : Configuring Bot' )

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

												'name' : 'help' ,
												'brief' : 'SquatchOS Help' ,
												'description' : 'SquatchOS Help' ,
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

	@bot.event
	async def on_ready():
		print('\nSquatchOS : Bot Started')
		print('\nSquatchOS : SquatchOS Started')

	print ( '\nSquatchOS : Bot Configured' )

	return bot

def run ( bot , token ) :

	print ( '\nSquatchOS : Starting Bot' )

	bot.load_extension('SquatchOS.cog')

	bot.load_extension('SquatchShell.cog')

	bot.run(token)

	SquatchOS.stop ()
