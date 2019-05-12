import sys

alphabet = {'a':2, 'b':3, 'c':5}
msg = sys.argv[1]
msg1 = msg.split("#")
lst = []
a = 0
b = 1
while a != len(msg1) :
	b = b * alphabet[msg1[a]]
	a += 1
print(b)
