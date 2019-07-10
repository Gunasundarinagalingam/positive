aaz,bby=input().split()
aaz=int(aaz)
bby=int(bby)
d=''
u=2
if(aaz+bby<=3):
    for i in range(0,aaz+bby):
        if(i%2!=0):
            d=d+'0'
        else:
            d=d+'1'
else:    
    for i in range(0,aaz+bby):
        if(i==u):
            d=d+'0'
            if(u==bby):
                u=u+2
            else:
                u=u+3
        else:
            d=d+'1'
x=len(d)-1
if(int(d[x])==0):
    print('-1')
elif aaz==1 and bby==2: print("011")
else:
    print(d)
