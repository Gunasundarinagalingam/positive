#a
import sys,string
nn = int(input())
L = [ int(x) for x in input().split()]
s2 = 0
for i in range(0,nn) :
    s2 = s2 + L[i]

for j in range(nn-2,-1,-1) :
    for i in range(0,nn-j) :
        li, ri = i,j+i
        sum1 = sum(L[li:ri+1])
        if sum1 > s2 :
            s2 = sum1
print(s2)
