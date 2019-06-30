num1=int(input())
num2=list(map(int,input().split()))
for x in range(0,num1-2):
 for y in range(x+1,num1-1):
  for z in range(y+1,num1):
   if(num2[x]+num2[y]==num2[z]):
    print(num2[x], num2[y], num2[z])
