indu=input()
ll=[indu[i] for i in range(len(indu)) if i%2==0]
l1l=[indu[i] for i in range(len(indu)) if i%2!=0]
for j in range(len(indu)//2):
  print(l1l[j]+ll[j],end="")
