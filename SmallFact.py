#http://ideone.com/AFSJRj
#small factorial

from sys import stdin

def fact(n):
	f = 1
	for i in range(2,n+1):
		f *= i
	return f

t = stdin.buffer.readline()

a = list(map(int, stdin.buffer.read().split()))

for x in a:
	print( fact(x) )
