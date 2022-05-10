#include<iostream>
#include<algorithm>
using namespace std;
 
int f[5][1005];

int main()
{   
	for(int i = 1; i <= 3; i ++)
	   for(int j = 1; j <= 1000; j ++)
			f[i][j] = j;               // 无论有几部手机，运气最差时的测试次数就是楼层的高度                         
			                           // (第一部手机从第一层摔到最后一层，都不坏)                        
	
	for(int i = 2; i <= 3; i ++)
	   for(int j = 1; j <= 1000; j ++)
          for(int k = 1; k < j; k ++)           
               f[i][j] = min(f[i][j], max(f[i- 1][k - 1], f[i][j - k]) + 1);  // min 表示最佳策略，max 表示最差运气 
	
	cout << f[3][1000] << endl;
	return 0;
}