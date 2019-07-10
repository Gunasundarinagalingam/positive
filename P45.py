vvj=input()
if vvj==vvj[::-1]:
    print("yes")
else:
    val=vvj.strip("0")
    if val==val[::-1]:
        print("yes")
    else:
        val=vvj.lstrip("0")
        if val==val[::-1]:
            print("yes")
        else:
            print("no")
