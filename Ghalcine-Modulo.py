import uuid
import random

def Cipher(mot, alphCipher):
	"""Cipher function. Use like wordToCipher.Ghalcine.Cipher(115456272781)"""
	alphabet = alphCipher[0]
	msg = mot
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
		
	final = str(mot) +"/"+ordre1
	return final



def Decipher(mot, alphaDecipher):
	"""Decipher function. Use like Ghalcine.Decipher("3151522/1.3.2.0.4", alphabet)"""
	alphabet = alphaDecipher[1]
	msg = mot.split("/")[0]
	ordre = mot.split("/")[1].split(".")
	msg = int(msg)
	lst = fin =[]
	d = alphaDecipher[0]["a"]
	while msg > 1 :
	    while msg % d==0 :
	        msg = msg // d
	        lst.append(d)
	    d += 1
	a = 0
	while a != len(lst) :
	    lst[a] = alphabet[lst[a]]
	    a += 1
	a = 0
	while a != len(lst):
	    lst[a] = str(lst[a])
	    a += 1
	dico = {}
	a = 0
	while a != len(ordre):
	    dico.update({int(ordre[a]) : lst[a]})
	    a += 1
	fin = []
	a = 0
	b = len(dico)
	while a != b:
	    fin.append(min(dico[min(dico)]))
	    dico.pop(min(dico))
	    a += 1
	fin1 = ""
	for x in fin:
	    fin1 = fin1+x
	return fin1



def Alphagen(choix):
	"""Alphabet and primary numbers blender function, use like Ghalcine.alphagen('gen')"""
	primes = []
	charset = 'azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN01234567890.+-*/²&é"\'(-è_çà)=~#{[|`\\^@]^$ù*,;:!¨%µ?./§<>\n'
	if choix == "gen":
	    a = uuid.uuid1().int
	elif type(choix) == 0:
	    a = int(choix)
	a2 = a
	while a != a2 + len(charset):
	    b = 0
	    c = 2
	    while c < int(a**0.5):
	        if a%c:
	            b = 1
	            c = int(a**0.5)
	        else:
	            pass
	        if b == 1:
	            primes.append(a)
	        c += 1
	    a += 1
	random.shuffle(primes)
	chars = list(charset)
	fin1 = []
	i = 0
	fin = {}
	for x in charset:
		fin.update({x:primes[i]})
		i += 1
		a += 1
	fin1.append(fin)
	i = 0
	fin = {}
	for x in charset:
		fin.update({primes[i]:x})
		i += 1
	fin1.append(fin)
	return fin1