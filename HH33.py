#a
ss=input()
l=[0]
if "ab" not in ss:
	print("0")
else:
	for i in range(len(ss)):
		c=1
		for j in range(i,len(ss)-1):
			if ss[j]=="a" and ss[j+1]=="b":
				c=c+1
			elif ss[j]=="b" and ss[j+1]=="a":
				c=c+1
			else:
				l.append(c)
				c=1
				break
		if ss[i]=="a":
			l.append(c)
		else:
			l.append(c-1)
	print(max(l))
