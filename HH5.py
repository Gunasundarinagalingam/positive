num=list(map(str,input()))
ss=ee=0
for i in range(0,len(num)-1):
  q=num[i]
  if int(q)!=0:
   for j in range(i+1,i+2):
    q=q+num[j]
    if int(q)<27 and int(q)>0: ss=ss+1
    elif int(q)==0: ss=ss-1
    else: break
if ss!=1: ee=ss%2
print(ss+ee+1)
