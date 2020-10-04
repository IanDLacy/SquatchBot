import SquatchOS
import SquatchShell

from discord.ext import commands

@ commands.command	(

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
@ SquatchShell.Command (  )
async def terminate ( self , context ) :
	ss = context.bot.get_cog('SquatchShell')
	if ss.viewport :
		await ss.viewport.delete()
	await context.bot.logout ()
	return None