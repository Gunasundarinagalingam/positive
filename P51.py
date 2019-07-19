def n6(l3):
        nn3=1
        for x in range(0,len(l3)-1):
                if l3[x]!=l3[x+1]:
                        nn3=nn3+1
                else:
                    break
        return nn3
num3=int(input())
l3=list(map(int,input().split()))
for x in range(0,len(l3)):
        if l3[x]>0:
                l3[x]=1
        else:
             l3[x]=0
nn4=""
for x in range(0,len(l3)):
        k=l3[x::]
        nn4=nn4+str(n6(k))+" "
print(nn4.strip())
