from discord.ext import commands

def setup ( bot ) :

	@commands.command	(

				name = 'Terminate' ,
				brief = 'Terminate SquatchBot' ,
				description = 'Terminate SquatchBot' ,
				aliases =	[

						'close'  ,
						'die'    ,
						'end'    ,
						'exit'   ,
						'kill'   ,
						'leave'  ,
						'logout' ,
						'quit'

						] ,
				usage = '[ No Arguments ]' ,
				help =	'Running this command causes the SquatchBot process to disconnect and end.' \
					'\nIf SquatchBot is running from a daemon, it will restart shortly.' ,
				enabled = True ,
				hidden = False ,
				rest_is_raw = False ,
				require_var_positional = False ,
				ignore_extra = True ,
				cooldown_after_parsing = False

				)
	async def terminate ( context ) :
		await context.send ( '```fix\n> Exit```' )
		await context.bot.logout (  )
		print ( '\nSquatchBot : Exit\n' )

	bot.add_command ( terminate )

	print ( '\nSquatchBot : Extension Setup [ commands.terminate ]' )

def teardown ( bot ) :
	print ( '\nSquatchBot : Extension Teardown [ commands.terminate ]')
