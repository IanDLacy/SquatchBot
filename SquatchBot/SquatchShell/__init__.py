import functools

from discord.ext import commands

import SquatchOS

class command (  ) :

	def __init__ ( self ) :
		pass

	def __call__ ( self , function ) :

		@functools.wraps ( function )
		async def decorator ( *args , **kwargs ) :

			for arg in args :

				if arg.__class__.__name__ == 'Context' :

					await arg.message.delete (  )
					await arg.send	(

							'```fix\n' + str ( await function ( *args , **kwargs ) ) + '\n```' ,
							delete_after = 15

							)
					break
		return decorator
