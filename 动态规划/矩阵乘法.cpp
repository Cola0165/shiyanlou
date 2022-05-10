#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int m, s, n;
    while(cin>>m>>s>>n)
    {
        // vector<vector<int> > matrix1(m);//注意> > 两个'>'之间保留空格
        // for(int i = 0; i < m; i++)
        //     matrix1[i].resize(s);
        // vector<vector<int> > matrix2(s);//注意> > 两个'>'之间保留空格
        // for(int i = 0; i < s; i++)
        //     matrix2[i].resize(n);

        vector<vector<int> > matrix1(m,vector<int>(s));
        vector<vector<int> > matrix2(s,vector<int>(n));

        for(int i = 0; i < m; i++)
        for(int j = 0; j < s; j++)
            cin>>matrix1[i][j];

        for(int i = 0; i < s; i++)
        for(int j = 0; j < n; j++)
            cin>>matrix2[i][j];

        vector<vector<int> > matrix3(m, vector<int>(n));
        for(int raw1 = 0; raw1 < m; raw1++)
        {//矩阵乘法
            for(int column2 = 0; column2 < n; column2++)
            {
                for(int column1 = 0; column1 < matrix1[0].size(); column1++)
                matrix3[raw1][column2] += matrix1[raw1][column1] * matrix2[column1][column2];
            }
        }

        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(j != n - 1)
                    cout<<matrix3[i][j]<<' ';
                else
                    cout<<matrix3[i][j];
            }
            cout<<endl;
        }
    }
    return 0;
}