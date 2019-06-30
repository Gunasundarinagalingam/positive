num1=int(input())
num2=0
array=input().split(" ")
array.sort(reverse=True)
for a in range(0,num1):
    num2*=10
    num2+=int(array[a])
print(num2)
