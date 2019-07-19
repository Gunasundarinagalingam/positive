sss=input()
t=input()
c=1
n=len(sss)
for i in range(0,len(t)-n,n):
	if t[i:i+n]==sss:
		c=c+1
print(c)
