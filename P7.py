num1=int(input())
num2=1
while(num2<=num1 and num2*2<=num1):
    num2=num2*2
if(num2==num1):
    print("0")
else:    
    print(num1-num2)
