num=int(input())
num1=list(map(int,input().split()))
oi=max(num1)
x,y=0,0
for i in range(0,len(num1)-1):
 for j in range(i+1,len(num1)):
  if abs(num1[i]+num1[j])<oi:
   x,y=num1[i],num1[j]
   oi=abs(x+y)
print(y,x)
