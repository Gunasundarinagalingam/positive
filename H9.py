akk,bkk=map(int,input().split())
ln=[]
for i in range(akk+1,bkk+1):
  if i>1:
    for j in range(2,i):
      if(i%j==0):
        break
    else:
      ln.append(j)
print(len(l)+1)
