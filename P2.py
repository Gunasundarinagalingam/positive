from itertools import combinations
num,num1=map(int,input().split())
g=len(str(num))
a=list(combinations(str(num),g-num1))
a=(sorted(a))
l="".join(a[0])
print(l)
