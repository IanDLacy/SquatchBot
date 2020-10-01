from discord.ext import commands

import SquatchShell

@commands.command	(

			name = 'ping' ,
			brief = 'SquatchOS Latency' ,
			description = 'Ping' ,
			usage = '[ No Arguments ]' ,
			help =	'This command returns the current latency between Discord and SquatchOS.' ,
			enabled = True ,
			hidden = False ,
			rest_is_raw = False ,
			require_var_positional = False ,
			ignore_extra = True ,
			cooldown_after_parsing = False

			)
@SquatchShell.command (  )
async def ping ( self , context ) :
	return f'Pong!\n{ round ( self.bot.latency*1000 ) } ms'
