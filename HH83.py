Nn=input()
k=""
m=0
for i in range(len(Nn)-1):
    k=""
    if Nn[i]==Nn[i+1]:
        k=k+Nn[:i+1]+Nn[i+2:]
        if int(k)>m:
            m=int(k)
print(m)
