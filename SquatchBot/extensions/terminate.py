from discord.ext import commands

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
			# enabled = True ,
			# parent = [ Command ] ,
			# cog = [ Cog ] ,
			# hidden = True ,
			# rest_is_raw = [ bool (False) ] ,
			# require_var_positional = [ bool (false) ] ,
			# ignore_extra = [ bool (True) ] ,
			# cooldown_after_parsing = [ bool (False) ] ,
			# cog_name = [ str ] ,
			)
async def terminate (context) :
	"""Equivalent To [brief=[str]], But Gets Overridden"""
	await context.send ( '```fix\n> Exit```' )
	await context.bot.logout()
	print ( '\nSquatchBot : Exit\n' )

def setup(bot) :
	bot.add_command(terminate)
	print('\nSquatchBot : Extension Setup [ Terminate ]')

def teardown(bot) :
	print('\nSquatchBot : Extension Teardown [ Terminate ]')
