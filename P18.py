hhhh,eeee=map(int,input().split())
ttt=[]
xy=0
for i in range(hhh):
    ttt.append(list(map(int,input().split())))   
for i in range(hhhh):
    for j in range(eeee-1):
        for k in range(j+1,eeee+1):
            if ttt[i][j:k]==[1]*len(ttt[i][j:k]):
                 if all(ttt[p+i][j:k]==[1]*len(ttt[p+i][j:k]) for p in range(len(ttt[i][j:k])-1)):
                     if len(ttt[i][j:k])>xy:
                        xy=len(ttt[i][j:k])
if len(ttt)==1 and len(ttt[0])==1 and ttt[0][0]==1:
    print(1)
for i in range(xy):
    print(*[1]*xy)
