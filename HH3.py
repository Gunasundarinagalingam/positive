num=int(input())
l=[int(x) for x in input().split()[:num]]
nl=[]
for i in range(0,int(len(l))):
    if(i==l[i]):
        nl.append(i)
if(int(len(nl)))!=0:
    for u in nl:
        print(u,end=" ")
else:
    print(-1)
