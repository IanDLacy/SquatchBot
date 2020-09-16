from discord.ext import commands

def setup ( bot ) :

	@commands.command	(

				name = 'Extension' ,
				brief = 'Extension Management' ,
				description = 'Extension Management' ,
				aliases =	[

						'ext'  ,
						'x'

						] ,
				usage = '[ Load | Unload | Reload ] <module>' ,
				help =	'Use this command to manage SquatchBot\'s extensions.' ,
				enabled = True ,
				hidden = False ,
				rest_is_raw = False ,
				require_var_positional = False ,
				ignore_extra = True ,
				cooldown_after_parsing = False

				)
	async def extension ( context , action='' , name='' ) :

		message = ''

		if action == '' :
			message += 'Action Required :\n\'load\' | \'unload\' | \'reload\'\n'
		elif action != 'load' and action != 'unload' and action != 'reload' :
			message += 'Invalid Action :\n\'load\' | \'unload\' | \'reload\'\n'

		if name == '' :
			message += 'Name Required : Specify Name\n'

		try :
			if action == 'load' and name != '' :
				bot.load_extension ( f'extensions.{name}' )
			elif action == 'unload' and name != '' :
				bot.unload_extension ( f'extensions.{name}' )
			elif action == 'reload' and name != '' :
				bot.reload_extension ( f'extensions.{name}' )
		except :
			message += f'extension {action} {name} : Fail'
		else :
			if message == '' :
				message += f'extension {action} {name} : Success'

		await context.send ( message )

	bot.add_command ( extension )

	print ( '\nSquatchBot : Extension Setup [ commands.extension ]' )

def teardown ( bot ) :
	print ( '\nSquatchBot : Extension Teardown [ commands.extension ]')
