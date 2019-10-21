class UnfoundElementError(Exception):
	pass
class InvalidKeyFormatError(Exception):
	pass

class GAY:
	def __init__(self):
		self.key = None
		self.word = None

	def cipher(self):
		try:
			alphabet = self.key[0]
			msg = self.word
			lst = []
			a = 0
			mot = 1
			while a != len(msg) :
			    mot = mot * alphabet[msg[a]]
			    a += 1
			xc = [(index,item) for item,index in enumerate(msg)]
			ry = sorted(xc, key = lambda msg : msg[0])
			y = [item[0] for item in ry]
			ordre = [0] * len(msg)
			for index,item in enumerate(ry):
			    ordre[item[1]] = index
			for x in range(0, len(ordre)):
				ordre[x] = str(ordre[x])
			return str(mot)+"/"+".".join(ordre)
		except KeyError:
			raise UnfoundElementError("A caracter is missing in key.")

	def decipher(self):
		try:
			alphabet = self.key[1]
			msg = int(self.word.split("/")[0])
			ordre = self.word.split("/")[1].split(".")
			for x in range(0,len(ordre)):
				ordre[x] = int(ordre[x])
			msgF =[]
			d = 2
			while msg > 1 :
			    while msg % d==0 :
			        msg = msg // d
			        msgF.append(d)
			    d += 1
			d = 0
			while d != len(msgF):
			    msgF[d] = alphabet[msgF[d]]
			    d += 1
			final = ""
			d = 0
			while d != len(msgF):
			    final += msgF[int(ordre[d])]
			    d += 1
			return final
		except KeyError:
			raise UnfoundElementError("A primary number is missing in key.")

def isPrime(prime):
	lst = []
	d = 2
	while d <= prime ** 0.5 :
		if prime % d != 0:
			pass
		elif prime % d == 0:
			return False
		d += 1
	return True

def KeyGen(charset, primeToTest):
	"""Key generator, use like KeyGen([yourCharset], [aNumber>0])"""
	if list(charset) != sorted(list(charset)):
		raise InvalidKeyFormatError("Charset should be in alphabetical order.")
	if len(list(charset)) != len(set(list(charset))):
		raise InvalidKeyFormatError("Caracter should not have more than one occurrence.")
	primes = []
	dic = {}
	while len(primes) != len(charset):
		if isPrime(primeToTest):
			primes.append(primeToTest)
		else:
			pass
		primeToTest += 1
	a = 0
	while a != len(charset):
		dic.update({charset[a]:primes[a]})
		a += 1
	final = []
	final.append(dic)
	dic = {}
	a = 0
	while a != len(charset):
		dic.update({primes[a]:charset[a]})
		a += 1
	final.append(dic)
	return final
#test
