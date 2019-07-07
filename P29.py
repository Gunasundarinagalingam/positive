inpp=int(input())
i=0
x=0
bb1=[]
while i<90 and i<inpp:
  s=0
  for j in str(inpp-i):
    s+=int(j)
  if s+(inpp-i)==inpp:
    x+=1
    bb1.append(inpp-i)
  i+=1
print(x)
for i in bb1:
  print(i)
