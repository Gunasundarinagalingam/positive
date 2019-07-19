#a
bb,s=map(str,input().split("|"))
c=input()
if  len(bb)>len(s):
    if len(bb)==len(s)+len(c):
        print(bb+"|"+s+c)
elif len(bb)<len(s):
     if len(s)==len(bb)+len(c):
        print(bb+c+"|"+s)
elif len(bb)==len(s) and len(c)>1 or (len(s) or len(bb)):
    print("impossible")
