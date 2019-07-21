nnn,mm=map(int,input().split())
k=max(nnn,mm)
pp=[]
for i in range(1,k):
    if nnn%i==0 and mm%i==0:
        pp.append(i)
if len(pp)==1:
    print("yes")
else:
    print("no")
