num1,num2=input().split()
r=0
if len(num1)>len(num2):
 num1,num2=num2,num1
p=0
while p<len(num1):
 r+=(ord(num2[p])-ord(num1[p]))
 p+=1
for p in range(p,len(num2)):
 r+=ord(num2[p])-ord('a')+1
print(r)
