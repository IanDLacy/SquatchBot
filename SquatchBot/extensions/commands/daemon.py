from discord.ext import commands

def setup ( bot ) :

	@commands.group	(

			name = 'Daemon' ,
			brief = 'Control Other Bots' ,
			description = 'SquatchBot Daemon' ,
			aliases =	[ 'd' ] ,
			usage = '[ Deploy | Start | Stop | Remove ]' ,
			help =	'This command and its subcommands are used to deploy and control other bots via SquatchBot.' ,
			enabled = True ,
			hidden = False ,
			rest_is_raw = False ,
			require_var_positional = False ,
			ignore_extra = True ,
			cooldown_after_parsing = False

			)
	async def daemon ( context ) :
		# Yes I know this is super 'dangerous', I'll work security into it later lol .
		await context.send('daemon')

	@daemon.command (  )
	async def deploy ( context ) :
		# Zip must have an __main__.py in the root .
		await context.send('deploy')

	@daemon.command (  )
	async def start ( context , package ) :
		# Bot will be automatically restarted if it crashes or ends itself .
		await context.send('start')

	@daemon.command (  )
	async def stop ( context , package ) :
		await context.send('stop')

	@daemon.command (  )
	async def remove ( context , package ) :
		await context.send('remove')

	bot.add_command(daemon)

	print ( '\nSquatchBot : Extension Setup [ commands.daemon ]' )

def teardown ( bot ) :
	print ( '\nSquatchBot : Extension Teardown [ commands.daemon ]' )
