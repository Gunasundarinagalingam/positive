import math
aa,aa1=map(int,input().split())
cc=[]
bb=list(map(int,input().split()))
for i in range(0,aa1):
    l,h=map(int,input().split())
    cc.append([l,h])
for i in cc:
    d=i[0]-1
    e=i[1]-1
    print(math.gcd(bb[d],bb[e]))
