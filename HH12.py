try:
    shh,ssi=map(int,input().split())
    ars=list(map(int,input().split()))
    ars1=sorted(ars)
    print(ars1[shh-ssi])
except ValueError:
    print("invalid")
