stt,n=input().split()
stt=str(stt)  
n=int(n)
li=[] 
for i in range(len(stt)-n+1):
	li.append(stt[i:i+n])  
print(*li)
