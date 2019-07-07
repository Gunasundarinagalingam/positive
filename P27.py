AA,BB=map(int,input().split())
CC=list(map(int,input().split()))
pp=list(map(int,input().split()))
qq=[]
rr=0
for i in range(AA):
    x=pp[i]/CC[i]
    qq.append(x)
while BB>=0 and len(qq)>0:
    mindex=qq.index(max(qq))
    if BB>=CC[mindex]:
        rr=rr+pp[mindex]
        BB=BB-CC[mindex]
    CC.pop(mindex)
    pp.pop(mindex)
    qq.pop(mindex)
print(rr)
