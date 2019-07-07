def avgg(list_aa):
    return sum(list_aa)//len(list_aa)


aa = int(input())
ls = [int(x) for x in input().split()]
l1 = []
for i in range(len(ls)-1):
    if avgg(ls[0:i+1]) == avgg(ls[i+1:aa]):
        l1.append('yes')      
    else:
        l1.append('no')
if 'yes' in l1:
    print('yes')
else:
    print('no')
