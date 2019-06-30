vhh=int(input())
vjj=list(map(int,input().split()))
num=si=[]
for i in range(0,vhh):
    num=list(bin(vjj[i]))
    num=num[2:]
    si.append(num)
si=sorted(si)
si=si[::-1]
for i in range(0,vhh):
    yy=1
    zz=0
    for j in range(len(si[i])-1,-1,-1):
        zz=zz+(int(si[i][j])*yy)
        yy=yy*2
    print(zz)
