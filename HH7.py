num1=int(input())
num2=list(map(int,input().split()))
l=[]
for i in range(0,len(num2)):
 if num2[i]%2==0 and i%2==1:
  l.append(num2[i])
 elif num2[i]%2==1 and i%2==0:
  l.append(num2[i])
print(*l,sep=' ')   
