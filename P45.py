aaa = int(input())
while aaa%10==0:
    aaa=aaa//10
aa=str(aaa)
b=aaa[::-1]
if aaa==b:
    print("yes")
else:
    print("no")
