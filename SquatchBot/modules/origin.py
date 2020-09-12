file = './SquatchBot/state/origin'
handle = ''

try :
	handle = open ( file , 'rt' )
except :
	print ('\nSquatchBot : Incorrect Working Directory')
	exit ('\nSquatchBot : Exit\n')

if handle :
	print(f'\nSquatchBot : {handle.readline().strip()}')
	handle.close()
