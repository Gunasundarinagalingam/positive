num=int(input())
s=0
i=0
while num > 0:
  i=num%10
  num=num//10
  s=s+i
print(s)
