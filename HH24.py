nn=[int(s) for s in input().split()]
mm=[int(s) for s in input().split()]
f=1
for i in range(nn[0]):
    for j in range(nn[0]):
        if i!=j:
            if nn[1]==mm[i]+mm[j]:
                f=0
                break
if f==0:
    print('YES')
else:
    print('NO')
