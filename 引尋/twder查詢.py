import twder

def currencySearch(search):
	dollorTuple = twder.now(search)
	reply = '{}\n美金的即期賣出價uweee! : {}'.format(dolloarTuple[0],dolloarTuple[4])
	return reply