nn=int(input())
l=[1000,500,100,50,10,1]
c=0
while nn>0:
  for i in range(0,len(l)):
    if nn>=l[i]:
      nn=nn-l[i]
      c+=1
      break
print(c)
