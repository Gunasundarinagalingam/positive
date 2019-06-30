num,num1=map(int,input().split())
vv={int(vv) for vv in input().split()}
kk={int(kk) for kk in input().split()} 
if(kk.issubset(vv)):
  print("YES")
else:
  print("NO")
