aaz,bby=map(int,input().split())
hh=list(map(int,input().split()))
hh.sort()
hh.reverse()
aaz=bby
z=0
for i in hh:
    if(aaz>=i):
        nm=int(aaz/i)
        z=z+nm
        aaz=aaz-nm*i
    if aaz==0:
        break
if(aaz==0):
   print(z)
else:
     print("it's not posiible to select coins in such a way that they sum upto",S)  
