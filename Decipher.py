import sys

#Decipher

alphabet = {2:'a', 3:'b', 5:'c'}
msg = sys.argv[1]
msg = int(msg)
lst = []
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
lst = str(lst)
print(lst)