from itertools import permutations
Nn=input()
k=permutations(Nn)
l=[]
m=(-1)
a="abcdefghijklmnopqrstuvwxyz"
if a==Nn:
  print(Nn)
elif Nn==a[::-1]:
  print("-1")
else:
    Nn=tuple(Nn)
    for i in k:
        l.append(i)
    for i in l:
        if i>Nn:
            m=i
            break

    for i in l:
        if i>Nn and i<m:
            m=i

    if m==-1:
        print("-1")
    else:
        for i in m:
            print(i,end="")
