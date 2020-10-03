import SquatchOS

@ SquatchOS.extension (  )
def setup ( bot ) :
	bot.add_cog ( SquatchOS ( bot ) )

@ SquatchOS.extension (  )
def teardown ( bot ) :
	bot.remove_cog ( 'SquatchOS' )

@ SquatchOS.Cog ( package = 'SquatchOS.cog' )
class SquatchOS :
	def __init__ ( self , bot ) :
		self.bot = bot
		self.bot.help_command.cog = self
