class GAY:
	def __init__(self):
		self.key = None
		self.word = None

	def cipher(self):
		alphabet = self.key[0]
		msg = self.word
		lst = []
		a = 0
		mot = 1
		while a != len(msg) :
		    mot = mot * alphabet[msg[a]]
		    a += 1
		lst = sorted(set(msg))	
		ordre = []
		for letter in lst:
			ordre += [index for index, value in enumerate(msg) if value == letter]
		ordre1 = str(ordre[0])
		a = 1
		while a != len(ordre):
			ordre1 = ordre1+"."+str(ordre[a])
			a += 1
			return [mot, ordre]

	def decipher(self):
		alphabet = self.key[1]
		msg = self.word[0]
		ordre = self.word[1].split(".")
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
	primes = final =[]
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
	dic = {}
	final.append(dic)
	a = 0
	while a != len(charset):
		dic.update({primes[a]:charset[a]})
		a += 1
	final.append(dic)
	return final
