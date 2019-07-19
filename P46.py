ppp3=int(input())
qqq3=list(map(int,input().split()))
a3=0
b3=0
qqq3.sort(reverse=True)
for i in qqq3:
  qqq3=a3+i
  if b3>qqq3:
    a3=qqq3
  else:
    a3=b3
    b3=qqq3
print(a3,b3)
