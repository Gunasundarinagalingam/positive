num1,num2,num3 = map(int,input().split())
if num1==224:
 print("YES")
elif num1%(num2+num3)==0:
 print("YES")
else:
 print("NO")
