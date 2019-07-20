nn,k=map(int,input().split())
s=0
if k<=nn:
    while nn>0 and nn>=k:
        nn=nn-k
        s=s+1
print(s)
