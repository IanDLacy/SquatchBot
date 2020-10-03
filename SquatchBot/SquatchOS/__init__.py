import functools
import importlib
import os

from discord.ext import commands

import SquatchOS.origin
import SquatchOS.log
import SquatchOS.token
import SquatchOS.bot

def start () :

	print ( '\nSquatchOS : Starting SquatchOS' )

	SquatchOS.origin.find ()

	SquatchOS.log.initiate ()

	SquatchOS.bot.run ( SquatchOS.bot.configure () , SquatchOS.token.acquire () )

def stop () :

	print ( '\nSquatchOS : Stopping SquatchOS' )

	# Future Stuff Goes Here Maybe

	exit ( '\nSquatchOS : SquatchOS Stopped \n' )

def extension ( *args , **kwargs ) :

	def decorator ( function ) :

		@ functools.wraps ( function )
		def decorated ( *args , **kwargs ) :

			function ( *args , **kwargs )
			print ( f'\nSquatchOS : Extension { function.__name__.capitalize() } [ { function.__module__ } ]' )

		return decorated

	return decorator

class Cog :
	def __init__ ( self , path = None , package = None , attributes = None ) :

		self.path = ( path or './' ) + ( package.replace ( '.' , '/' ) if package else '' )
		self.package = package
		self.attributes = attributes or {}

	def __call__ ( self , base ) :

		importlib.invalidate_caches ()

		self.attributes.update	(

					{

					key : value
					for file
					in os.listdir ( self.path )
					if file != '__init__.py'
					and file.endswith ( '.py' )
					for ( key , value )
					in importlib . import_module ( f'{ self.package or base.__name__ }.{ file[:-3] }' ) . __dict__ . items ()
					if isinstance ( value , ( commands.Group , commands.Command ) )

					}

					)

		return type ( base.__name__ , ( base , commands.Cog ) , self.attributes )
