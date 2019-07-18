import sys
alphabet = {2:'a', 3:'b', 5:'c'}
msg = sys.argv[1]
ordre = sys.argv[2]
msg = int(msg)
lst = fin =[]
d = 2
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
a = 0
b = len(dico)
while a != b:
	fin.append(min(dico[min(dico)]))
	dico.pop(min(dico))
	a += 1
print(fin)
