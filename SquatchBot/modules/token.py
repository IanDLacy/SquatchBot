file = './SquatchBot/state/token'
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
		token = input ( '\nSquatchBot : Discord API Token :\n' )
	except :
		exit ('\nSquatchBot : Exit\n')

	try :
		handle = open ( file , 'wt' )
	except :
		print ('\nSquatchBot : Unable To Open Or Create Token File')
		exit ('\nSquatchBot : Exit\n')

	handle.write(token)
	handle.close()

print ('\nSquatchBot : Token Acquired')
