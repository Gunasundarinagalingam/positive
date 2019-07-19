#a
nn=int(input())
x=[]
c=0
for i in range(nn):
  x.append(list(map(int,input().split())))
res=[]
for i in range(nn+1):
  if i==0:
    res.append(list("0"*(nn+2)))
  else:
    s="0"
    for j in range(nn):
      s=s+str(x[i-1][j])
    res.append(list(s+"0"))
res.append(list("0"*(nn+2)))
for i in range(len(res)):
  for j in range(len(res)):
    if res[i][j]=="1" and res[i-1][j]==res[i+1][j]==res[i][j-1]==res[i][j+1]==res[i+1][j+1]==res[i+1][j-1]==res[i-1][j+1]==res[i-1][j-1]=="0":
      c+=1
print(c)
