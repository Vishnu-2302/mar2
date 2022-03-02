def intake(k):
	h=[]
	r=int(input('number of rows : '))
	c=int(input('enter number of columns : '))
	for i in range(r):
		row=[]
		for j in range(c):
			v=int(input())
			row.append(v)
		h.append(row)
	k.extend(h)
def ans(k):
	c=len(k)
	r=len(k[0])
	for i in range(c):
		for j in range(r):
			k[i][j]=A[i][j]+B[i][j]
	print('result = ')
	for i in range(c):
		for j in range(r):
			print(k[i][j],end=' ')
		print()

A=[]
B=[]
intake(A)
intake(B)
result=[]
r=len(A)
c=len(A[0])
for i in range(r):
	row=[]
	for j in range(c):
		row.append(0)
	result.append(row)
ans(result)