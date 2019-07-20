NN=int(input())
l=[]
for i in range(NN):
	l1=[int(x) for x in input().split()]
	m=sum(l1)
	l.append(m)
m=sum(l)/(NN*NN)
print("%.6f" %m)
