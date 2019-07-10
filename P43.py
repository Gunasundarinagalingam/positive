tt1 = int(input())
aa1 = list(map(int,input().split()))
s,l = 0,[]
b1 = [x for x in range(1,tt1+1)]
for i in aa1:
  if i in b1:
    b1.remove(i)
kh = 0
for i in range(0,tt1-1):
  p = aa1[i]
  for j in range(i+1,tt1):
    if p == aa1[j]:
      if p < b1[kh]:
        aa1[j] = b1[kh]
        s += 1
      else:
        aa1[i] = b1[kh]
        s += 1
      kh += 1
print(s)
print(*aa1)
