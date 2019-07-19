#a
ss=input()
n=len(ss)

def check_palindrome(ss,n):
    if ss==ss[-1:-n-1:-1]:
        n-=1
        ss=ss[0:n]
        check_palindrome(ss,n)
    else:
        print(ss)


check_palindrome(ss,n)   
