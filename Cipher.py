import sys

alphabet = {"a":2, "b":3, "c":5, "d":7}
msg = sys.argv[1]
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

print(mot, ordre1)
