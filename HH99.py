xx,y,z=map(int,input().split())
count=0
for i in range(xx,y+1):
   if str(z)in str(i):
       count+=1
print(count)
