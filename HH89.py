xX=str(input())
t=[]
for i in range(0,len(xX)):
    if(xX[i] not in t):
         t.append(xX[i])
t=t[::-1]
print(*t,sep="")
