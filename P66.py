ppp, qp, fp, k = map(int, input().split())
cnt = 0
d = qp-fp
if (d >= 0):
    s = (ppp-fp)*2
    for i in range (k):
        if (i == k-1):
             s =s/ 2
        if (d < s):
            d= qp
            cnt += 1
        d = d - s
        if (d < 0):
            cnt = -1
            break
        s = 2*ppp - s
    print (cnt)
else:
    print (-1)
