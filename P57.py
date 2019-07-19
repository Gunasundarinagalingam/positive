ppp,qqq=map(str,input().split())
count=0
for i in range(0,len(ppp)):
    for j in range(0,len(qqq)):
        if ppp[i]==qqq[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
