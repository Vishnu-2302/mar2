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
	for i in range(len(A)):
		for j in range(len(B[0])):
			for c in range(len(B)):
				k[i][j]=k[i][j]+A[i][c]*B[c][j]
	for i in range(len(A)):
		for j in range(len(A[0])):
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