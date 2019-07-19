aa1=int(input())
bb1=pow(2,aa1)
z1=[]
for i in range(bb1):  
    m1=bin(i).replace("0b","")
    z1.append(m1.zfill(aa1))
    z1.sort(key=(lambda x:x.count('1')))
for i in z1:
    print(i)
