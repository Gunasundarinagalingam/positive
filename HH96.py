import sys,string
def dgtSum(nn) :
    sum1 = 0
    while nn :
        sum1 += nn%10
        nn //= 10
    return sum1

nn = int(input())
if nn <= 9:
    print(nn)
    sys.exit()
a = nn // 9
b = nn % 9
if b :
    s = str(b) + str('9') * a
else :
    s = str('9') * a
print(s)
