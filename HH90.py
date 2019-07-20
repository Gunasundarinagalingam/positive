nN = input()
c,n,m = 0,'',0
for i in range(0,len(nN)):
  c = 1
  for j in range(i+1,len(nN)):
    if nN[i]==nN[j]:
      c += 1
    else:
      break
  if c>m:
    m = c
    n = nN[i]
print(n,m)
