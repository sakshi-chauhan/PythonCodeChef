#COOLING - http://ideone.com/gPcDpY

t = int(input())

for k in range(t):
	count = 0

	n = int(input())

	wt = []
	lim = []

	wt = list( map(int, input().split()) )
	lim = list( map(int, input().split()) )

	wt.sort()
	lim.sort()

	j = 0

	for i in range(n):
		if j<n:
			while (j<n) and (wt[i]>lim[j]):
				j += 1

			if (j < n):
				count += 1

		j += 1

	print(count)
