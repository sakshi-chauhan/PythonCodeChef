__author__ = 'Samsung'
x,y = input().split()

x = float(x)
y = float(y)

if (x%5==0) and ( x < y ) and ( y - x - 0.5 >= 0 ):
	print( y - x - 0.5 )
else:
	print(y)
