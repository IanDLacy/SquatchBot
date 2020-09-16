from discord.ext import commands

def setup ( bot ) :

	@commands.command	(

				name = 'Ping' ,
				brief = 'SquatchBot Latency' ,
				description = 'Ping' ,
				usage = '[ No Arguments ]' ,
				help =	'This command returns the current latency between Discord and SquatchBot.' ,
				enabled = True ,
				hidden = False ,
				rest_is_raw = False ,
				require_var_positional = False ,
				ignore_extra = True ,
				cooldown_after_parsing = False

				)
	async def ping ( context ) :
		await context.send ( f'```fix\nPong!\n{ round ( bot.latency*1000 ) } ms```' )

	bot.add_command ( ping )

	print ( '\nSquatchBot : Extension Setup [ commands.ping ]' )

def teardown ( bot ) :
	print ( '\nSquatchBot : Extension Teardown [ commands.ping ]')
