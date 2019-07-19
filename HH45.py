nn=int(input())
l=list(map(int,input().split()))
c=0
for i in range(1,nn+1):
	if l.count(nn*i)>0:
		c=c+1
print(c)
