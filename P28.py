nn=int(input())
kk=list(map(int,input().split()))
kk.sort()
sin=0
sv=0
for i in range(len(kk)):
    if kk[i]>=sin:
        sv=sv+1
    sin=sin+kk[i]
print(sv)
