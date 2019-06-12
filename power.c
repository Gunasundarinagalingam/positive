#include<stdioh>
int main()
{
  int i,N,K;
  long power=1;
  scanf("%d",&N);
  scanf("%d",&K);
  for(i=1;i<=N;i++)
  {
    power=power*N;
  }
  printf("%d",power);
  return 0;
}
