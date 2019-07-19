import java.util.*;
public class ReverseList
{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		int nn = in.nextInt();
		int arr[] = new int[nn];
		for(int i=0 ; i<nn ; i++)
			arr[i] = in.nextInt();
		reverse(arr,nn);
	}
	public static void reverse(int arr[],int nn)
	{
		for(int i=nn-1 ; i>=0 ; i--)
		{
			if(i!=0)
				System.out.print(arr[i]+"->");
			else
				System.out.print(arr[i]);
		}
	}
}
