#a
import sys,string, math, itertools

nn,k = input().split()
nn,k = int(nn),int(k)
L = [ int(x) for x in input().split()]
#print(nn,k, L)
for i in range(0,nn) :
    if (86400-L[i]) >= k :
        print(i+1)
        sys.exit()
    k -= (86400-L[i])
