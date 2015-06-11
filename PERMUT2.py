# your code goes here

while( True ):

	t = int(input())

	if t==0:
		break

	b =[0]*t
	a =[]

	a = list(map(int,input().split()))

	for i in range(t):
		b[a[i]-1] = i+1

	if a==b:
		print("ambiguous")
	else:
		print("not ambiguous")