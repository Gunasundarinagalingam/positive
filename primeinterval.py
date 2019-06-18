num=int(input())
num1=int(input())
for val in range(num+1,num1+1):
  if val >1:
    for n in range(2,val):
      if val % n == 0:
        break
      else:
        print(val)
