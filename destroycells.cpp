#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t-->0)
	{
		if(t!=0)	cout<<endl;
		int n,m;
		cin>>n;
		cin>>m;
		for(int i=0;i<n*m;i++)
		{
			int a[n][m];
			for(int j=0;j<n;j++)	for(int k=0;k<m;k++)	a[j][k]=-1;
			int count=0,loose=i;
			for(int j=0;j<n;j++)	for(int k=0;k<m;k++)
			{
				if(loose!=i)	loose++;
				else{
					loose=0;
				if(a[j][k]==-1)
				{
					a[j][k]=0;
					count++;
				}
			}
			}
			loose=i;
			for(int k=0;k<m;k++)	for(int j=0;j<n;j++)	
			{
				if(loose!=i)	loose++;
				else{	
					loose=0;
				if(a[j][k]==-1)
				{
					a[j][k]=0;
					count++;
				}
			}
			}
			cout<<count;
			if(i!=n*m-1)	cout<<" ";
		}
		
	}

	return 0;
}