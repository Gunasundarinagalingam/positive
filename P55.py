#a
tt,s = map(int,input().split())
v = list(map(int,input().split()))
b,n = 0,[]
for i in range(0,len(v)):
  tt = i
  for p in range(0,len(v)):
    for l in range(0,s):
      if l == s-1:
        try:
          b += v[p+i]
        except IndexError:
            tt = t-1
            b +=v[tt]
      else:
        b += v[i]
    n.append(b)
    b = 0
for i in range(0,len(v),s):
  b = sum(v[i:i+s])
  n.append(b)
print(*sorted(set(n)))
