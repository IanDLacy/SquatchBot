import SquatchOS

def find () :

	print ('\nSquatchOS : Finding Origin')

	file = './SquatchOS/state/origin'
	handle = ''

	try :
		handle = open ( file , 'rt' )
	except :
		print ('\nSquatchOS : Incorrect Working Directory')
		SquatchOS.stop ()

	if handle :
		print(f'\nSquatchOS : {handle.readline().strip()}')
		handle.close()
