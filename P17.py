noo,hii=input().split()
noo=int(noo)
hii=int(hii)
count=0
l=list(map(int,input().split()))
for i in range(noo):
    for j in range(i+1,noo):
        ss=0
        ss=l[i]+l[j]
        if(ss==hii):
            count+=1
            break
if(count==1):
    print("yes")
else:
    print("no")
