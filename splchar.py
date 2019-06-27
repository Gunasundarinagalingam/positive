num=input()
xx=0
for i in range(len(num)):
  if(num[i].isdigit() or num[i].isalpha() or num[i]==(' ')):
    continue
  else:
    xx+=1
print(xx)
