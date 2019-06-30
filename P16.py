aab=int(input())
ccd=list(map(int,input().split()))
xy=[1]*aab
for i in range(aab):
    if i==0:
        if ccd[i]>ccd[i+1]:
            xy[i]=xy[i]+xy[i+1]
    elif i>0:
        if ccd[i]>ccd[i-1]:
            xy[i]=xy[i]+xy[i-1]
print(sum(xy))
