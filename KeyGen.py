import sys

def isPrime(prime):
	lst = []
	d = 2
	while d < prime ** 0.5 :
		if prime % d != 0:
			pass
		elif prime % d == 0:
			return False
		d += 1
	return True
	

charset = sys.argv[1]+" "
primeToTest = int(sys.argv[2])
choix = sys.argv[3]
primes = []
check = False
dic = {}

while len(primes) != len(charset):
	if isPrime(primeToTest):
		primes.append(primeToTest)
	else:
		pass
	primeToTest += 1

if choix == "cip":
	a = 0
	while a != len(charset):
		dic.update({charset[a]:primes[a]})
		a += 1
elif choix == "decip":
	a = 0
	while a != len(charset):
		dic.update({primes[a]:charset[a]})
		a += 1

print(dic)
