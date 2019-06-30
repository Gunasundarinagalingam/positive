ig,gi=map(int,input().split())
l1=[]
for i in range(ig,gi+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l1.append(i)
print(len(l1))
