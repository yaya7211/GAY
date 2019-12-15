import collections

class UnfoundElementError(Exception):
	pass

class GAY:
	def __init__(self):
		self.key = []

	def cypher(self, word):
		"""Cyphering method, use like GAY.cypher(\"wordToCypher\"), after setting the key in GAY().key"""
		try:
			alphabet = self.key[0]
			msg = word
			lst = []
			a = 0
			mot = 1
			while a != len(msg) :
			    mot = mot * alphabet[msg[a]]
			    a += 1
			######From Kwak######
			traduction_char = collections.defaultdict(list)
			swap = lambda tup: (tup[1], tup[0])
			char_index = dict(map(swap, enumerate(order)))
			for i, ch in enumerate(sorted(msg, key=lambda ch: char_index[ch])):
				traduction_char[ch].append(i)
			######From Kwak######
			ordre = list(map(lambda ch: traduction_char[ch].pop(), msg))
			for x in range(0, len(ordre)):
				ordre[x] = str(ordre[x])
			return str(mot)+"/"+".".join(ordre)
		except KeyError:
			raise UnfoundElementError("A caracter is missing in key.")

	def decypher(self, word):
		"""Decyphering method, use like GAY().decypher(\"wordtodecypher\"), after setting the key in GAY().key"""
		try:
			alphabet = self.key[1]
			msg = int(word.split("/")[0])
			ordre = word.split("/")[1].split(".")
			for x in range(0,len(ordre)):
				ordre[x] = int(ordre[x])
			######From stackoverflow######
			msgF =[]
			d = 2
			while msg > 1 :
			    while msg % d==0 :
			        msg = msg // d
			        msgF.append(d)
			    d += 1
			######From stackoverflow######
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

	def hash(self, word):
		"""hashing method, use like GAY().hash(\"wordtohash\"), after setting the key in GAY().key"""
		try:
			alphabet = self.key[0]
			msg = word
			lst = []
			a = 0
			mot = 1
			while a != len(msg) :
			    mot = mot * alphabet[msg[a]]
			    a += 1
			######From Kwak######
			traduction_char = collections.defaultdict(list)
			swap = lambda tup: (tup[1], tup[0])
			char_index = dict(map(swap, enumerate(order)))
			for i, ch in enumerate(sorted(msg, key=lambda ch: char_index[ch])):
				traduction_char[ch].append(i)
			######From Kwak######
			ordre = list(map(lambda ch: traduction_char[ch].pop(), msg))
			for x in range(0, len(ordre)):
				ordre[x] = str(ordre[x])
			ordre = "".join(ordre)
			mot = str(mot)
			x = len(mot)
			y = len(ordre)
			final = ""
			a = pgcd(x,y)
			if a != 1:
				x = x // a
				y = y // a
				for e in range(a):
					final += mot[:x-1]
					mot = mot[x-1:]
					final += ordre[:y-1]
					ordre = ordre[y-1:]
			else:
				a = 0
				while pgcd(x, y) == 1:
					try:
						mot = mot + mot[a]
					except IndexError:
						a = 0
					a += 1
				hash(mot)
			return final
		except KeyError:
			raise UnfoundElementError("A primary number is missing in key.")

########From developpez.net##########
def pgcd(a,b) :
	"""Plz don't use this func, it's for the dev""" 
   while a%b != 0 : 
      a, b = b, a%b 
   return b
########From developpez.net##########

def isPrime(prime):
	"""Plz don't use this func, it's for the dev"""
	lst = []
	d = 2
	while d <= prime ** 0.5 :
		if prime % d != 0:
			pass
		elif prime % d == 0:
			return False
		d += 1
	return True

def mDic(primes, charset):
	"""Plz don't use this func, it's for the dev"""
	dic = {}
	a = 0
	while a != len(charset):
		dic.update({charset[a]:int(primes[a])})
		a += 1
	final = []
	final.append(dic)
	dic = {}
	a = 0
	while a != len(charset):
		dic.update({int(primes[a]):charset[a]})
		a += 1
	final.append(dic)
	global order 
	order = charset
	return final

def key_gen(charset, prim):
	"""Key generator, use like KeyGen([yourCharset], [anInteger])"""
	if len(list(charset)) != len(set(list(charset))):
		raise InvalidKeyFormatError("Caracter should not have more than one occurrence.")
	global order #cipher
	global char
	char = charset
	order = list(charset)
	global primes
	primes = []
	while len(primes) != len(charset):
		if isPrime(prim):
			primes.append(prim)
		prim += 1
	return mDic(primes, charset)

def save_key(path):
	f = open(path, "w")
	f.write(char+"\n")
	p = ""
	for x in range(len(primes)):
		p += str(primes[x])+" "
	f.write(p)
	f.close()

def use_key(path):
	f = open(path, "r")
	a = f.read()
	charset = a.split("\n")[0]
	primes = a.split("\n")[1]
	primes = primes.split(" ")
	primes.pop(len(primes) - 1)
	return mDic(primes, charset)
