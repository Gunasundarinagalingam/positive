nn = int(input())
ll = list(map(int, input().split()))
maximum = 0
cnt = 0
aa = ll[0]
for i in range(0,nn-1):
    if aa < ll[i+1]:
        cnt +=1
        aa = ll[i+1]
    else:
        if max(ll[i+1:]) < aa:
            aa = ll[i+1]
print(cnt+1)
