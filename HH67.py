aa=input().split("#")
bb=input().split("#")
dd=aa[1]+aa[2]+aa[3]
e=bb[1]+bb[2]+bb[3]
if dd>e:
    print(aa[0])
elif e>dd:
    print(bb[0])
