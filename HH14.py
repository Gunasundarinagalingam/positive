from itertools import permutations
ssh=input()
ssh=list(ssh)
perm=permutations(ssh)
a=[]
for j in list(perm):
    a.append(''.join(list(j)))
b=list(set(a))
c=[]
for i in range(len(b)):
    c.append(b[i])
c.sort()
for i in range(len(c)):
    print(c[i])
