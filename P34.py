xx,yy=map(int,input().split())
mn=0
L=[]
for i in range(xx):
      L.append(input())
for i in range(xx):
      for j in range(yy-1):
            if(L[i][j]!='R' and L[i][j+1]!='R'):
                  mn+=3
            elif(L[i][j]!='G' and L[i][j+1]!='G'):
                  mn+=5
print(mn)
