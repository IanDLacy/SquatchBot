import SquatchShell

from discord.ext import commands

@ commands.group	(

		name = 'daemon' ,
		brief = 'Control Other Bots' ,
		description = 'SquatchOS Daemon' ,
		aliases =	[ 'd' ] ,
		usage = '[ Deploy | Start | Stop | Remove ]' ,
		help =	'This command and its subcommands are used to deploy and control other bots via SquatchOS.' ,
		enabled = True ,
		hidden = False ,
		rest_is_raw = False ,
		require_var_positional = False ,
		ignore_extra = True ,
		cooldown_after_parsing = False

		)
@ SquatchShell.Command (  )
async def daemon ( self , context ) :
	# Yes I know this is super 'dangerous', I'll work security into it later lol .
	return 'daemon'

@ daemon.command (  )
async def deploy ( self , context ) :
	# Zip must have an __main__.py in the root .
	return 'deploy'

@ daemon.command (  )
async def start ( self , context , package=None ) :
	# Bot will be automatically restarted if it crashes or ends itself .
	return 'start'

@ daemon.command (  )
async def stop ( self , context , package=None ) :
	return 'stop'

@ daemon.command (  )
async def remove ( self , context , package=None ) :
	return 'remove'
