ig=int(input())
le=[int(x) for x in input().split()[:ig]]
for u in le:
  if(le.count(u)==1):
    print(u,end=" ")
