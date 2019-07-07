nnn=int(input())
nnn1=2**nnn
ll1=[]
for i in range(0,nnn1):
    l=bin(i)[2:].zfill(nnn)
    if(len(l)<len(bin(2**nnn-1)[2:])):
        ll1.append([l.count("1"),l])
    else:
        ll1.append([l.count("1"),l])
ll1.sort()
for i in range(len(ll1)):
    print(ll1[i][1])
