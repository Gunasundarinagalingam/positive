vvj=input()
lis=list(set(vj))
xyy=1
h=0
check=False
while True:
    ch=lis[h]
    for j in range(0,len(vvj)-xy):
        if ch in vvj[j:j+xy]:
            check=True
        else:
            check=False
            h+=1
            if h>=len(lis):
             h=0
             xyy+=1
            break

    if check==True:
        break
print(xyy)
