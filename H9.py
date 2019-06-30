ig,gi=map(int,input().split())
ll=[]
for i in range(ig+1,gi+1):
  if i>1:
    for j in range(2,i):
      if(i%j==0):
        break
    else:
      ll.append(j)
print(len(l)+1)
