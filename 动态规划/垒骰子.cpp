#include<bits/stdc++.h>

#define MOD 1000000007
using namespace std;

int points[7] = {0, 4, 5, 6, 1, 2, 3};
int n, m;
int ban[36][2];
long long result;

bool judge(int point1, int point2)
{
    bool flag = true;
    for (int i = 0; i < m; i++)
    {
        int point3 = points[point2];
        if (point1 == ban[i][0] && point3 == ban[i][1])
        {

            flag = false;
            break;
        }
        if (point1 == ban[i][1] && point3 == ban[i][0])
        {

            flag = false;
            break;
        }
    }
    return flag;
}

void dfs(int cnt, int point)
{
    if (cnt == n)
    {
        result++;
        return;
    }
    for (int i = 1; i <= 6; i++)
    {
        if (judge(point, i))
        {
            cnt++;
            dfs(cnt, i);
            cnt--;
        }
    }
}

long long quickpow(int x, int N)
{
    int reg = x;
    int sum = 1;
    while (N)
    {
        if (N & 1)
        {
            sum = sum * reg;
        }
        reg *= reg;
        N = N >> 1;
    }
    return sum;
}
int main()
{

    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        cin >> ban[i][0] >> ban[i][1];
    }
    dfs(0, 0);

    long long temp = quickpow(4, n);
    cout << result * temp % MOD;
    return 0;
}

// #define MOD 1000000007

// typedef long long LL;
// LL dp[2][7];
// int n, m;
// bool conflict[7][7];
// map<int, int> op;

// void init()
// {
//     op[1] = 4;
//     op[4] = 1;
//     op[2] = 5;
//     op[5] = 2;
//     op[3] = 6;
//     op[6] = 3;
// }

// int main()
// {
//     init();
//     scanf("%d%d", &n, &m);
//     for (int i = 0; i < m; ++i)
//     {
//         int a, b;
//         scanf("%d%d", &a, &b);
//         conflict[a][b] = true;
//         conflict[b][a] = true;
//     }

//     for (int j = 1; j <= 6; ++j)
//     {
//         dp[0][j] = 1;
//     }

//     int cur = 0;

//     for (int level = 2; level <= n; ++level)
//     {
//         cur = 1 - cur;

//         for (int j = 1; j <= 6; ++j)
//         {
//             dp[cur][j] = 0;

//             for (int i = 1; i <= 6; ++i)
//             {
//                 if (conflict[op[j]][i])
//                     continue;
//                 dp[cur][j] = (dp[cur][j] + dp[1 - cur][i]) % MOD;
//             }
//         }
//     }

//     LL sum = 0;
//     for (int k = 1; k <= 6; ++k)
//     {
//         sum = (sum + dp[cur][k]) % MOD;
//     }

//     LL ans = 1;
//     LL tmp = 4;
//     LL p = n;

//     while (p)
//     {
//         if (p & 1)
//             ans = (ans * tmp) % MOD;
//         tmp = (tmp * tmp) % MOD;
//         p >>= 1;
//     }
//     printf("%lld\n", (sum * ans) % MOD);
//     return 0;
// }