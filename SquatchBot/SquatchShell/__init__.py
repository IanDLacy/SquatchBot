import functools

import SquatchOS

class Command (  ) :

	def __init__ ( self ) :
		pass

	def __call__ ( self , function ) :

		@ functools.wraps ( function )
		async def decorator ( self , context , *args , **kwargs ) :

			await context.message.delete ()

			content = '```fix\n' + str ( await function ( self , context , *args , **kwargs ) ) + '\n```'

			ss = self.bot.get_cog('SquatchShell')

			if ss.viewport :
				try :
					await ss.viewport.edit (content=content)
				except :
					ss.viewport = None
			else :
				ss.viewport = await context.send (content)

		return decorator
