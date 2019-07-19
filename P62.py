ppf=str(input())
ll=[]
t=""
r=0
for i in range(0,len(ppf)):
    for j in range(i,len(ppf)):
        t=t+ppf[j]
        if(t[::-1]==t):
            r=len(ppf)-len(t)
            ll.append(r)
    t=""
print(min(ll))
