N=int(input())
sum=0
temp = N
while temp > N:
  digit = temp % 10
  sum += digit ** 3
  temp // 10
if N == sum:
  print("yes")
else:
  print("no")
