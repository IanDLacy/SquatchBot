import SquatchOS

@ SquatchOS.extension (  )
def setup ( bot ) :
	bot.add_cog ( SquatchShell ( bot ) )

@ SquatchOS.extension (  )
def teardown ( bot ) :
	bot.remove_cog ( 'SquatchShell' )

@ SquatchOS.Cog ( package = 'SquatchShell.cog' )
class SquatchShell :
	def __init__ ( self , bot ) :
		self.bot = bot
