import logging

def initiate () :

	print ('\nSquatchOS : Initiate Logging')

	logger = logging.getLogger('discord')
	logger.setLevel(logging.DEBUG)
	handler = logging.FileHandler(filename='./SquatchOS/state/log',encoding='utf-8',mode='w')
	handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
	logger.addHandler(handler)

	print ('\nSquatchOS : Logging Initiated')
