tdd = int(input())
sMm1 = [ int(x) for x in input().split()]
tdd = len(sMm1)
scg = 0
for i in range(0,tdd-2) :
    for j in range(i+1, tdd-1):
        for k in range(j+1, tdd):
            if sMm1[i] > sMm1[j] > sMm1[k] :
                scg += 1
print(scg)
