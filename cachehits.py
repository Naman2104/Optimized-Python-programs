t = int(input())
for _ in range(t):
	n,b,m = map(int,input().split())
	x = list(map(int,input().split()))
	count = 0
	l = -1
	r = -1
	for i in x:
		if(l<=i and r>=i):
			continue
		l = (i//b)*b
		r = l + b - 1
		count += 1
	print(count)