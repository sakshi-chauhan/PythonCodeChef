__author__ = 'Samsung'
# your code goes here

t = int(input())

for i in range(0,t):
	str = input()
	#print(len(str))
	count = 0

	for j in range(0,len(str)):
		if ((str[j] == 'A')  or (str[j] == 'D') or (str[j] == 'R') or (str[j] == 'O') or (str[j] == 'P') or (str[j] == 'Q')):
			count += 1
		elif str[j] == 'B':
			count += 2

	print(count)
