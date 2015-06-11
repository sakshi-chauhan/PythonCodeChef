#ceilab - http://ideone.com/ukdawS

a,b = input().split()
a = int(a)
b = int(b)

c = a-b

if (c%10!=9):
	c += 1
else:
	c -= 1

print(c)
