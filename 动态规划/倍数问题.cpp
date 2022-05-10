#include <iostream>
using namespace std;

int n, k, ans = 0;
int temp[3], num[100005], vis[100005] = {0};

void dfs(int s)
{
    if (s == 3)
    {
        int t = temp[0] + temp[1] + temp[2];
        if (t % k == 0 && t > ans)
            ans = t;
        return;
    }
    else
    {
        for (int i = 0; i < n; i++)
        {
            if (!vis[i])
            {
                temp[s] = num[i];
                vis[i] = 1;
                dfs(s + 1);
                vis[i] = 0;
            }
        }
    }
}

int main()
{
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; i++)
        scanf("%d", &num[i]);
    dfs(0);
    printf("%d\n", ans);
    return 0;
}

// #include <cstring>

// #define FOR0(a, b) for (int i = a; i < b; ++i)
// #define FORE(a, b) for (int i = a; i <= b; ++i)
// typedef long long ll;
// typedef pair<int, int> pii;

// ll dp[2][4][1005];
// int n, k, a[100005], v[100005];
// int main()
// {
//     scanf("%d%d", &n, &k);
//     for (int i = 1; i <= n; ++i)
//     {
//         scanf("%d", &a[i]);
//         v[i] = a[i];
//         v[i] %= k;
//     }
//     memset(dp, -0x3f3f3f3f, sizeof dp);
//     dp[0][0][0] = 0;
//     int d = 0;
//     for (int i = 1; i <= n; ++i)
//     {
//         for (int j = 0; j < k; ++j)
//         {
//             for (int p = 0; p <= 3; ++p)
//             {
//                 if (i < p)
//                     continue;
//                 dp[d ^ 1][p][j] = max(dp[d ^ 1][p][j], dp[d][p][j]);
//                 if (p > 0)
//                     dp[d ^ 1][p][j] = max(dp[d ^ 1][p][j], dp[d][p - 1][((j - v[i]) % k + k) % k] + a[i]);
//             }
//         }
//         d ^= 1;
//     }
//     cout << dp[d][3][0] << endl;
//     return 0;
// }