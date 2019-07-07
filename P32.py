vvv,vvk=map(int,input().split())
sks=[]
for i in range(0,vvv):
    mn=[int(sv) for sv in input().split()]
    sks.append(sorted(mn))
for i in range(0,len(sks[0])):
  #print(sk[i])
  for j in range(0,len(sks)-1):
    if sks[j][i]>sks[j+1][i]:
      sks[j][i],sks[j+1][i]=sks[j+1][i],sks[j][i]
for i in sks:
  print(*i)
