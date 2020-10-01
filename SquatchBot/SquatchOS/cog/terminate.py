import SquatchOS
import SquatchShell

@SquatchOS.extension (  )
def setup ( bot ) :

	@bot.command	(

				name = 'terminate' ,
				brief = 'Terminate SquatchOS' ,
				description = 'Terminate SquatchOS' ,
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
				help =	'Running this command causes the SquatchOS process to disconnect and end.' \
					'\nIf SquatchOS is running from a daemon, it will restart shortly.' ,
				enabled = True ,
				hidden = False ,
				rest_is_raw = False ,
				require_var_positional = False ,
				ignore_extra = True ,
				cooldown_after_parsing = False

				)
	@SquatchShell.command (  )
	async def terminate ( context ) :
		await context.bot.logout (  )
		await SquatchOS.stop ()
		return 'Exit'

@SquatchOS.extension (  )
def teardown ( bot ) :
	bot.remove_command ( 'terminate' )
