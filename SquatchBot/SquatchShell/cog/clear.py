from discord.ext import commands

import SquatchShell

@commands.command	(

			name = 'clear' ,
			brief = 'Delete Messages' ,
			description = 'Delete Messages' ,
			aliases =	[ 'delete' ] ,
			usage = '<number>' ,
			help =	'Delete up to 8 messages at once, starting from the latest currently visible message.' ,
			enabled = True ,
			hidden = False ,
			rest_is_raw = False ,
			require_var_positional = False ,
			ignore_extra = True ,
			cooldown_after_parsing = False
			)
@ SquatchShell.command (  )
async def clear ( self , context , amount=0 ) :

	if amount > 8 or amount < 0 : amount = 0
	await context.channel.purge ( limit = amount )
	return f'Cleared { amount }'
