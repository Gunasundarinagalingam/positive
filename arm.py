num,num1=input().split()
num=int(num)
num1=int(num1)
for i in range(num,num+1):
  sum=0
  temp=num
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  if num == sum:
    print(num,end=" ")
    
