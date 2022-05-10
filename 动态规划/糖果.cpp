#include<bits/stdc++.h>
using namespace std;
int dp[1 << 20];
int ST[100];
int main()
{
    int n, m, k;
    cin >> n >> m >> k;
    int tot = (1 << m) - 1;
    memset(dp, -1, sizeof dp);
    for (int i = 0; i < n; i++)
    {
        int st = 0;
        for (int j = 0; j < k; j++)
        {
            int x;
            cin >> x;
            st |= (1 << x - 1);
        }
        dp[st] = 1;
        ST[i] = st;
    }
    for (int i = 0; i <= tot; i++)
    {
        if (dp[i] != -1)
        {
            for (int j = 0; j < n; j++)
            {
                int st = ST[j];
                if (dp[i | st] == -1 || dp[i | st] > dp[i] + 1)
                    dp[i | st] = dp[i] + 1;
            }
        }
    }
    cout << dp[tot];
    return 0;
}

// int n, m, k;
// int dp[1 << 20];
// vector<int> a;

// int main()
// {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);
//     cin >> n >> m >> k;
//     for (int i = 0; i < (1 << m); i++)
//     {
//         dp[i] = 9999;
//     }
//     for (int i = 0; i < n; i++)
//     {
//         int s = 0;
//         for (int i = 0; i < k; i++)
//         {
//             int temp;
//             cin >> temp;
//             s |= 1 << (temp - 1);
//         }
//         a.push_back(s);
//     }
//     dp[0] = 0;
//     for (int i = 0; i < n; i++)
//     {
//         for (int j = 0; j < (1 << m); j++)
//         {
//             if (dp[j] == 9999 || (j | a[i]) == j)
//                 continue;
//             dp[j | a[i]] = min(dp[j] + 1, dp[j | a[i]]);
//         }
//     }
//     if (dp[(1 << m) - 1] == 9999)
//         cout << -1;
//     else
//         cout << dp[(1 << m) - 1];
//     return 0;
// }