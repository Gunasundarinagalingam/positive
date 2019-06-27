num=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(0,num):
  print(l[i],end=" ")
