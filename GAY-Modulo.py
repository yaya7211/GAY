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



def Alphagen(mdp):
	"""Alphabet and primary numbers blender function, use like Ghalcine.alphagen(aPassWord)"""
	primes = []
	charset = 'azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN01234567890.+-*/²&é"\'(-è_çà)=~#{[|`\\^@]^$ù*,;:!¨%µ?./§<>\n'
	passList = {"a" : 0,
		"z" : 1,
		"e" : 2,
		"r" : 3,
		"t" : 4,
		"y" : 5,
		"u" : 6,
		"i" : 7,
		"o" : 8,
		"p" : 9,
		"q" : 10,
		"s" : 11,
		"d" : 12,
		"f" : 13,
		"g" : 14,
		"h" : 15,
		"j" : 16,
		"k" : 17,
		"l" : 18,
		"m" : 19,
		"w" : 20,
		"x" : 21,
		"c" : 22,
		"v" : 23,
		"b" : 24,
		"n" : 25,
		"A" : 26,
		"Z" : 27,
		"E" : 28,
		"R" : 29,
		"T" : 30,
		"Y" : 31,
		"U" : 32,
		"I" : 33,
		"O" : 34,
		"P" : 35,
		"Q" : 36,
		"S" : 37,
		"D" : 38,
		"F" : 39,
		"G" : 40,
		"H" : 41,
		"J" : 42,
		"K" : 43,
		"L" : 44,
		"M" : 45,
		"W" : 46,
		"X" : 47,
		"C" : 48,
		"V" : 49,
		"B" : 50,
		"N" : 51,
		"0" : 52,
		"1" : 53,
		"2" : 54,
		"3" : 55,
		"4" : 56,
		"5" : 57,
		"6" : 58,
		"7" : 59,
		"8" : 60,
		"9" : 61,
		"0" : 62,
		"." : 63,
		"+" : 64,
		"-" : 65,
		"*" : 66,
		"/" : 67,
		"²" : 68,
		"&" : 69,
		"é" : 70,
		"\"" : 71,
		"'" : 72,
		"(" : 73,
		"-" : 74,
		"è" : 75,
		"_" : 76,
		"ç" : 77,
		"à" : 78,
		")" : 79,
		"=" : 80,
		"~" : 81,
		"#" : 82,
		"{" : 83,
		"[" : 84,
		"|" : 85,
		"`" : 86,
		"\\" : 87,
		"^" : 88,
		"@" : 89,
		"]" : 90,
		"^" : 91,
		"$" : 92,
		"ù" : 93,
		"*" : 94,
		"," : 95,
		";" : 96,
		":" : 97,
		"!" : 98,
		"¨" : 99,
		"%" : 100,
		"µ" : 101,
		"?" : 102,
		"." : 103,
		"/" : 104,
		"§" : 105,
		"<" : 106,
		">" : 107,
		"\n" : 108}
	a = ""
	c = 0
	while len(a) != len(mdp):
		a += str(passList[mdp[c]])
		c += 1
	a = int(a)
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
