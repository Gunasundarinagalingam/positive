numm,kk=map(int,input().split())
l = list(map(int,input().split()))
count = 0
for i in range(0,len(l)):
    if (l[i]+kk)<=5:
        count+=1
print(count//3)
