num=int(input())
if num <= 1000:
  for i in range(2,num):
    if num % i == 0:
      print("no")
     else:
      print("yes")
