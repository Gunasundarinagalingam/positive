vvj=input()
f=0
for i in range(0,len(vvj)-1):
  for j in range(i+1,len(vvj)):
    if vvj[i]<vvj[j]:
      f=1
      print(vvj[j:])
      break
  if f==1:
    break
else:
  print(vvj)      
