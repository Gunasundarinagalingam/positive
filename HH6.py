num1=int(input())
num2=list(map(int,input().split()))
tj=[]
for x in range(num1):
 for i in range(x+1,len(num2)):
  if(num2[i]==num2[x]):
    tj.append(num2[x])

if (len(tj)==0):
    print("unique")
else:
    print(tj[0])
