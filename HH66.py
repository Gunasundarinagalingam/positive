numberr=int(input())
li=list(map(str,input().split()))
numberrtofind=input()
count=0
for value in li:
  if numberrtofind==value[0:2]:
    count+=1
print(count)
