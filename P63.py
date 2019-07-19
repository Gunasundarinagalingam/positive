ppa=input()
qs=[]
for i in ppa:
  if i not in qs:
    qs.append(i)
  else:
    break  
print(len(qs))
