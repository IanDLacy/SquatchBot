import SquatchOS

def acquire (  ) :

	print ('\nSquatchOS : Acquiring Token')

	file = './SquatchOS/state/token'
	handle = ''
	token = ''

	try :
		handle = open ( file , 'rt' )
	except :
		pass

	if handle :
		token = handle.readline().strip()
		handle.close()

	if token == '' :
		try :
			token = input ( '\nSquatchOS : Discord API Token :\n' )
		except :
			SquatchOS.stop ()

		try :
			handle = open ( file , 'wt' )
		except :
			print ('\nSquatchOS : Unable To Open Or Create Token File')
			SquatchOS.stop ()

		handle.write(token)
		handle.close()

	print ('\nSquatchOS : Token Acquired')

	return token
