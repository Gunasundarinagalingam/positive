vjj,vkk=map(int,input().split())
lis=list(map(int,input().split()))
vjj=[]
lis.insert(0,0)
for y in range(vkk):
     v=[]
     sumup=0
     cc,dd=map(int,input().split())
     for i in range(cc,dd+1):         
         sumup^=lis[i]     
     vjj.append(sumup)
for y in vjj:
    print(y)
