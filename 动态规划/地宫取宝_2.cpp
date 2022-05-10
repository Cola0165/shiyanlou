#include <iostream>
#include <cstring>

using namespace std;

int n, m, k;
int data[55][55];

long long ans;
long long mod = 1000000007;
void dfs(int x, int y, int max, int count)
{
    if (x == n || y == m)
    {
        return;
    }
    int cur = data[x][y];
    if (x == n - 1 && y == m - 1)
    {
        if (count == k || (count == k - 1 && cur > max))
        {
            ans++;
            if (ans > mod)
            {
                ans %= mod;
            }
        }
    }
    if (cur > max)
    {
        dfs(x, y + 1, cur, count + 1);
        dfs(x + 1, y, cur, count + 1);
    }

    dfs(x, y + 1, max, count);
    dfs(x + 1, y, max, count);
}

int main()
{
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < m; ++j)
        {
            scanf("%d", &data[i][j]);
        }
    }

    dfs(0, 0, -1, 0);

    printf("%lld\n", ans);
    return 0;
}

// const int N = 55;
// const int MOD = 1e9 + 7;
// int dp[N][N][13][14];
// int g[N][N];
// int n, m, k;

// int main()
// {
//     cin >> n >> m >> k;
//     for (int i = 1; i <= n; i++)
//     {
//         for (int j = 1; j <= m; j++)
//         {
//             cin >> g[i][j];
//             g[i][j]++;
//         }
//     }
//     dp[1][1][1][g[1][1]] = 1;
//     dp[1][1][0][0] = 1;
//     for (int i = 1; i <= n; i++)
//     {
//         for (int j = 1; j <= m; j++)
//         {
//             for (int u = 0; u <= k; u++)
//             {
//                 for (int v = 0; v <= 13; v++)
//                 {
//                     dp[i][j][u][v] = (dp[i][j][u][v] + dp[i - 1][j][u][v]) % MOD;
//                     dp[i][j][u][v] = (dp[i][j][u][v] + dp[i][j - 1][u][v]) % MOD;
//                     if (u > 0 && v == g[i][j])
//                     {
//                         for (int c = 0; c < v; c++)
//                         {
//                             dp[i][j][u][v] = (dp[i][j][u][v] + dp[i - 1][j][u - 1][c]) % MOD;
//                             dp[i][j][u][v] = (dp[i][j][u][v] + dp[i][j - 1][u - 1][c]) % MOD;
//                         }
//                     }
//                 }
//             }
//         }
//     }
//     int res = 0;
//     for (int i = 0; i <= 13; i++)
//         res = (res + dp[n][m][k][i]) % MOD;
//     cout << res << endl;
//     return 0;
// }

// int n, m, k;
// int data[55][55];
// typedef long long LL;

// LL ans;
// LL mod = 1000000007;
// LL cache[55][55][15][15];

// LL dfs2(int x, int y, int max, int count)
// {

//     if (cache[x][y][max + 1][count] != -1)
//     {
//         return cache[x][y][max + 1][count];
//     }
//     LL ans = 0;
//     if (x == n || y == m || count > k)
//     {
//         return 0;
//     }
//     int cur = data[x][y];
//     if (x == n - 1 && y == m - 1)
//     {
//         if (count == k || (count == k - 1 && cur > max))
//         {
//             ans++;
//             if (ans > mod)
//             {
//                 ans %= mod;
//             }
//         }
//         return ans;
//     }
//     if (cur > max)
//     {
//         ans += dfs2(x, y + 1, cur, count + 1);
//         ans += dfs2(x + 1, y, cur, count + 1);
//     }

//     ans += dfs2(x, y + 1, max, count);
//     ans += dfs2(x + 1, y, max, count);

//     cache[x][y][max + 1][count] = ans % mod;
//     return ans % mod;
// }

// void dfs(int x, int y, int max, int count)
// {
//     if (x == n || y == m || count > k)
//     {
//         return;
//     }
//     int cur = data[x][y];
//     if (x == n - 1 && y == m - 1)
//     {
//         if (count == k || (count == k - 1 && cur > max))
//         {
//             ans++;
//             if (ans > mod)
//             {
//                 ans %= mod;
//             }
//         }
//     }
//     if (cur > max)
//     {
//         dfs(x, y + 1, cur, count + 1);
//         dfs(x + 1, y, cur, count + 1);
//     }

//     dfs(x, y + 1, max, count);
//     dfs(x + 1, y, max, count);
// }

// int main()
// {
//     scanf("%d%d%d", &n, &m, &k);
//     for (int i = 0; i < n; ++i)
//     {
//         for (int j = 0; j < m; ++j)
//         {
//             scanf("%d", &data[i][j]);
//         }
//     }

//     memset(cache, -1, sizeof(cache));
//     printf("%lld\n", dfs2(0, 0, -1, 0));
//     return 0;
// }