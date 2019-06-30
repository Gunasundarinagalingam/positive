aaa,bbb=map(int,input().split())
ccc=[]
ddd=[]
eee=[int(aaa) for aaa in input().split()]
for i in range(0,bbb):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        ddd.append(eee[j])
    vj=sum(ddd)
    ccc.append(vj)
print(ccc[0])
for x in range(1,len(ccc)):
    print(ccc[x]- ccc[x- 1])
