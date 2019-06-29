ig,gi=map(str,input().split())
if(len(ig)!=len(ig)):
  print("no")
c=[ig.count(i) for i in ig]
d=[gi.count(i) for i in gi]
if c==d:
  print("yes")
else:
  print("no")
