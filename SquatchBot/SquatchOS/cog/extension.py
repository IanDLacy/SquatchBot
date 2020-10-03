import SquatchShell

from discord.ext import commands

@ commands.command	(

					name = 'extension' ,
					brief = 'Extension Management' ,
					description = 'Extension Management' ,
					aliases =	[

								'ext'  ,
								'x'

								] ,
					usage = '[ Load | Unload | Reload ] <module>' ,
					help =	'Use this command to manage SquatchOS extensions.' ,
					enabled = True ,
					hidden = False ,
					rest_is_raw = False ,
					require_var_positional = False ,
					ignore_extra = True ,
					cooldown_after_parsing = False

					)
@ SquatchShell.command (  )
async def extension ( self , context , action='' , name='' ) :

	message = ''

	if action == '' :
		message += 'Action Required :\n\'load\' | \'unload\' | \'reload\'\n'
	elif action != 'load' and action != 'unload' and action != 'reload' :
		message += 'Invalid Action :\n\'load\' | \'unload\' | \'reload\'\n'

	if name == '' :
		message += 'Name Required : Specify Name\n'

	try :
		if action == 'load' and name != '' :
			context.bot.load_extension ( name )
		elif action == 'unload' and name != '' :
			context.bot.unload_extension ( name )
		elif action == 'reload' and name != '' :
			context.bot.reload_extension ( name )
	except :
		message += f'extension {action} {name} : Fail'
	else :
		if message == '' :
			message += f'extension {action} {name} : Success'

	return message