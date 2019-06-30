from collections import Counter
num1=int(input())
num2=list(map(int,input().split()))
num3=Counter(num2)
list=[]
for a in num3.items():
  if(a[1] != 1):
    print(a[0],end = " ")
for b in num3.items():
  list.append(b[1])
if(max(list) == 1):
  print("unique")
