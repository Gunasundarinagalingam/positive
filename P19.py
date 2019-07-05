vjj=int(input())
vkk=list()
for i in range(vjj):
    bm=input().split()
    bm=[int(d) for d in bm]
    for j in bm:
        vkk.append(j)
vkk.sort()
for i in vkk:
    print(i,end=" ")
