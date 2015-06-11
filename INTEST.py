# your code goes here

from sys import stdin

n,k =  map(int, stdin.buffer.readline().split())

count = 0


a=list(map(int, stdin.buffer.read().split()))

for x in a:
	if x%k==0:
		count = count + 1

print(count)

