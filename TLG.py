# your code goes here

n = int(input())

max = 0
p1 = 0
p2 = 0

for i in range(0,n):
	x,y = input().split()
	x = int(x)
	y = int(y)

	p1 += x
	p2 += y

	if p1 > p2:
		l = p1-p2
		pos = 1

	else:
		l = p2-p1
		pos = 2

	if l > max:
		max = l
		w = pos

print(w,max)

