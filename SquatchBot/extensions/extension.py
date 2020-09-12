import discord
from discord.ext import commands

class Extension ( commands.Cog ) :
	def __init__ ( self , client ) :
		self.client = client

	@ commands.command (  )
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
				self.client.load_extension ( f'extensions.{name}' )
			elif action == 'unload' and name != '' :
				self.client.unload_extension ( f'extensions.{name}' )
			elif action == 'reload' and name != '' :
				self.client.reload_extension ( f'extensions.{name}' )
		except :
			message += f'extension {action} {name} : Fail'
		else :
			if message == '' :
				message += f'extension {action} {name} : Success'

		await context.send ( message )

def setup ( client ) :
	client.add_cog ( Extension ( client ) )
