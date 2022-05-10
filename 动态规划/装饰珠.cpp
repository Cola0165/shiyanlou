#include<iostream>
#include<cstring>
using namespace std;
constexpr size_t MAXN = 55, MAXS = 305, MAXM = 1e4 + 5;
int n[MAXN], cnt[5], Lv[MAXM], p[MAXM], w[MAXM][MAXN];
int dp[MAXM][MAXS];
int m;

inline void Read()
{
    ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    for (int i = 1; i <= 6; i++)
    {
        cin >> n[i];
        for (int j = 1, x; j <= n[i]; j++)
        {
            cin >> x;
            cnt[x]++;
        }
    }
    cin >> m;
    for (int i = 1; i <= m; i++)
    {
        cin >> Lv[i] >> p[i];
        for (int j = 1; j <= p[i]; j++)
            cin >> w[i][j];
    }
}

inline int DP()
{
    memset(dp, 0x80, sizeof dp), dp[0][0] = 0;
    int ans = 0, sum = 0, tot = 0;
    for (int L = 4; L >= 1; L--)
    {
        sum += cnt[L];
        for (int i = 1; i <= m; i++)
            if (Lv[i] == L)
            {
                tot++;
                for (int k = 0; k <= sum; k++)
                    dp[tot][k] = dp[tot - 1][k];
                for (int j = 1; j <= p[i]; j++)
                    for (int k = j; k <= sum; k++)
                        dp[tot][k] = max(dp[tot][k], dp[tot - 1][k - j] + w[i][j]);
            }
    }
    for (int i = 0; i <= sum; i++)
        ans = max(ans, dp[tot][i]);
    return ans;
}

signed main()
{
    Read();
    cout << DP();
}
