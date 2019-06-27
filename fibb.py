num=int(input())
fibo,g=0,1
print(g,end=" ")
for i in range(1,n):
  yy=fibo+g
  print(yy,end=" ")
  fibo,g=g,yy
