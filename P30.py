hhh=input()
abc=0
for i in range(0,len(hhh)):
    sv=hhh[0:i]+hhh[i+1::]
    if int(sv)%8==0:
        acb=1
        break
if abc==1:
    print("yes")
else:
    print("no")
