aa = int(input())
bb = list(map(int,input().split()))
cc = []
ee = []
for i in enumerate(bb):
  cc.append(i)
for i in range(0,len(bb)):
  for j in range(0,len(bb)):
    for k in range(0,len(bb)):
      if(cc[i][1] < cc[j][1] < cc[k][1]):
        if(cc[i][0] < cc[j][0] < cc[k][0]):
          d = [cc[i][1],cc[j][1],cc[k][1]]
          ee.append(d)
if(len(ee) != 0):
  print(len(ee))
else:
  print("0")
