nn1=input()
ll1=list(set(nn1))
x=1
a=0
check=False
while True:
    ch=ll1[a]
    for y in range(0,len(nn1)-x):
        if ch in nn1[y:y+x]:
            check=True
        else:
            check=False
            a=a+1
            if a>=len(ll1):
             a=0
             x=x+1
            break

    if check==True:
        break
print(x)
