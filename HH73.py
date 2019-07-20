ss=input()
a=input()
k=min(len(ss),len(a))
l=""
if k==len(ss):
    for i in range(k-1):
        for j in range(i+1,k):
            if ss[i:j+1] in a:
                if len(ss[i:j+1])>=len(l):
                    l=ss[i:j+1]
else:
    for i in range(k-1):
        for j in range(i+1,k):
            if a[i:j+1] in ss:
                if len(a[i:j+1])>=len(l):
                    l=a[i:j+1]
print(l)
