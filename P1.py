ls1=int(input())
b1=[]
for i in range(0,ls1):
 inpu=input()
 b1.append(inpu)
li=[]
for i in zip(*b1):
 if(i.count(i[0])==len(i)):
  li.append(i[0])
            
 else:
  break
print(''.join(li))
