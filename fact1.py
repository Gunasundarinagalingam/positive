N=int(input())
fact=1
if N <= 20:
  for i in range(1,N+1):
    fact=fact*i
print(fact)
