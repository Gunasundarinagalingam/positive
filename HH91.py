ss1=input()
n=1
if len(ss1)==1:
    print("yes")
else:
    for j in ss1:
        if ss1.count(j)==len(ss1):
            print("no")
            n=0
            break
    if n==1:
        print("yes")
