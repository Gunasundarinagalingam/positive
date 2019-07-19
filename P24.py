aaa1=int(input())
bbb1=pow(2,aaa1)
z1=[]
for i in range(bbb1):  
    m1=bin(i).replace("0b","")
    z1.append(m1.zfill(aaa1))
    z1.sort(key=(lambda x:x.count('1')))
for i in z1:
    print(i)
