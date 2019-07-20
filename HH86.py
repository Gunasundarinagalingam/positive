def difff(y):
    s=0
    for i in range(0,len(y)):
        if y[i]=='2':
            s=s+1
    return s
n=int(input())
s=0
for i in range(0,n+1):
    y = list(str(i))
    s=s+difff(y)
print(s)
