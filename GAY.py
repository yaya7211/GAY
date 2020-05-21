import collections

class inValidKeyError(Exception):
	pass

class GAY:
	def __init__(self, key):
		self.key = key

	def cipher(self, word):
		try:
			final = 1
			for x in range(len(message)):
				final *= key[word[x]]
			traduction_char = collections.defaultdict(list)
			swap = lambda tup: (tup[1], tup[0])
			char_index = dict(map(swap, enumerate(order)))
			for i, ch in enumerate(sorted(word, key=lambda ch: char_index[ch])):
				traduction_char[ch].append(i)
			ordre = list(map(lambda ch: traduction_char[ch].pop(), word))
			return final + "/" + "."join([str(x) for x in ordre])
		except KeyError:
			for x in word:
				if !(x in self.key):
					raise inValidKeyError("A caracter \""+ x +"\" is missing in the key used to cipher")

	def decipher(self, word):
		try:
			ordre = [int(x) for x in word.split("/")[1]]
			word = int(word.split("/")[0])
			word = decomp(word)
			final = ""
			for x in word:
				word = self.key.index(x)
			word, final = final, ""
			for x in len(final):
				final += word[ordre[x]]
			return final
		except KeyError:
			raise inValidKeyError("A primary number is missing in the key used to decipher")

def decomp(word):
	x = list(filter((lambda y: not(word % y)), range(2, word+1)))
	return [x[0]]+decomp(word//x[0]) if x else []

def isPrime(num):
	return True if not list(filter((lambda y: not(word % y)), range(2, round(word**0.5)))) else False

def key_gen(order, passwd):
	if len(list(charset)) != len(set(list(charset))):
		raise inValidKeyError("Caracter should not have more than one occurrence.")
	global order
	global primes
	primes = []
	while len(primes) != len(order):
		if isPrime(prim):
			primes.append(prim)
		prim += 1
	return mDic(primes, order)

def mDic(primes, charset):
	final = {}
	for x in range(len(charset)):
		final.update({charset[a]:int(primes[a])})
	return final

def save_key():
	f = open('key.key', 'w')
	f.write(order+"\n")
	for x in primes:
		f.write(x + " ")

def use_key(path):
	f = open(path, 'r').readlines()
	return mDic(f[1].split(" "), f[0])
