import sys

alphabet = {2:"a", 3:"b", 5:"c",7:"d"}
msg = int(sys.argv[1])
ordre = sys.argv[2].split(".")
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

final = []
d = 0
while d != len(msgF):
    final.append(msgF[int(ordre[d])])
    d += 1

print(final) 
