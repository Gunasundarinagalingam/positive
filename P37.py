nnn3 = int(input())
L3 = [int(x) for x in input().split()]
nnn3 = len(L3)
if nnn3==1 :
    print()
   
cnt = 0
for i in range(1,nnn3-1) :
    if ((L3[i] > L3[i-1]) and (L3[i] > L3[i+1])) or ((L3[i] < L3[i-1]) and (L3[i] < L3[i+1])):
        cnt += 1
print(cnt)
