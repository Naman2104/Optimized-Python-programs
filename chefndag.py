t = int(input())

dict1={}
result=[]

def makenode(i):
	global dict1
	global result
	curr_list = result.copy()

	if(i > len(dict1)):
		return 0
	if(len(dict1[i]) == 0):
		return 0
	for j in dict1[i]:
		if j not in result:
			result[i-1] = j
			makenode(i+1)
			if(curr_list.count(0) > result.count(0)):
				curr_list = result.copy()
			result[i-1] = 0
	result = curr_list.copy()


for _ in range(t):
	n,k=map(int,input().split())
	l=[]
	for i in range(k):
		l.append(list(map(int,input().split())))

	c = []
	result=[]
	dict1={}
	for i in range(1,n+1):
		dict1[i] = []
		result.append(0)
	for j in range(0,n):
		curr_num = l[0][j]
		for i in range(j+1,n):
			find_num = l[0][i]
			for m in range(1,k):
				if find_num not in l[m][l[m].index(curr_num):]:
					break
			else:
				dict1[curr_num].append(find_num)

	makenode(1)
	print(result.count(0))
	print(*result)