num=[int(i) for i in input().split()]
mm=num[0]
nn=num[1]
num=[int(i) for i in input().split()]
xx=0
for i in num:
  if i == nn:
    xx=xx+1
if xx == 0:
  print("no")
else:
  print("yes")
