ssh=int(input())
ssi=list(map(int,input().split()))
c1=[]
for i in range(0,ssh):
    d=ssi[i:]
    e=max(d)
    if ssi[i]==e:
        c1.append(ssi[i])
print(*c1)
print(max(ssi))
