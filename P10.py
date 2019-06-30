aadp=int(input())
bbdp=[int(i) for i in input().split()]
xxdp=0
for i in range(aadp):
   for j in range(i):
      if bbdp[j]<bbdp[i]:
         xxdp+=bbdp[j]
print(xxdp)   
