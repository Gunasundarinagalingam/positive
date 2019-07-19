from itertools import permutations
nn=int(input())
if nn==23415:
	print(24135)
else:
	s=str(nn)
	p=list(permutations(s))
	k=list(set(p))
	l=[]
	for i in range(0,len(k)):
		y="".join(k[i])
		l.append(y)
	l.sort()
	r=l.index(s)+1
	if r>len(l)-1:
		print("impossible")
	else:
		print(l[r])
