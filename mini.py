n=int(input())
ls=list(map(int,input().split()))
b=ls[0]
for i in range(n):
  for j in range(i+1,n):
    if(b>ls[j]):
      b=ls[j]
print(b)
