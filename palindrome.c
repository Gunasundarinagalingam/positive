#include<stdio.h>
int main()
{
int n,r=0,t;
scanf("%d",&num);
t=n;
while(t!=0)
{
r=r*10;
r=r+t%10;
t=t/10;
}
if(n==r)
printf("yes");
else
printf("no");
return 0;
}
