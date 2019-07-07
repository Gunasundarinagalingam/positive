pp=int(input())
rr=list(map(int,input().split()))
x=rr[0:pp:2]
y=rr[1:pp:2]
if sum(x)>=sum(y):
  print(sum(x))
else:
  print(sum(y))
