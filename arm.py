num=int(input())
num1=int(input())
for i in range(num,num+1):
  sum=0
  temp=num
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  if num == sum:
    print(num)
    
