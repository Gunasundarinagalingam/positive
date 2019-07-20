ss1=input()
s2=input()
T=""
r=[]
n=0
for i in range(len(ss1)-1):
	for j in range(i,len(ss1)):
		if ss1[i:j+1] in s2:
			if len(ss1[i:j+1])>=len(T):
				T=ss1[i:j+1]
				a,b=i,j
print(ss1[a:b+1])
