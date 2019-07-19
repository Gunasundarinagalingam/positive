#a
nn1=int(input())
li=[]
a=nn1//2+nn1
for i in range(1,nn1+1):
    if i%2==0:
        li.append(i)
for i in range(1,nn1+1):
    if i%2!=0:
        li.append(i)
for i in range(1,nn1+1):
    if i%2==0:
        li.append(i)
print(a)
print(*li)
