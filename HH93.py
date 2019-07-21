Nnn=input()
temp=""
f=0
for i in range(len(Nnn)):
  if Nnn[i]==" ":
    temp+=Nnn[i]
  elif f==0:
    temp+=Nnn[i].upper()
    f=1
  elif f==1:
    temp+=Nnn[i]
    f=0
print(temp)
