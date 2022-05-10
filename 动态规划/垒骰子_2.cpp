#include<bits/stdc++.h>
using namespace std;

#define MOD 1000000007

typedef long long LL;
LL dp[2][7];
int n, m;
bool conflict[7][7];
map<int, int> op;

void init()
{
    op[1] = 4;
    op[4] = 1;
    op[2] = 5;
    op[5] = 2;
    op[3] = 6;
    op[6] = 3;
}

struct M
{
    LL a[6][6];

    M()
    {
        for (int i = 0; i < 6; ++i)
        {
            for (int j = 0; j < 6; ++j)
            {
                a[i][j] = 1;
            }
        }
    }
};

M mMultiply(M m1, M m2)
{
    M ans;

    for (int i = 0; i < 6; ++i)
    {
        for (int j = 0; j < 6; ++j)
        {
            ans.a[i][j] = 0;
            for (int k = 0; k < 6; ++k)
            {
                ans.a[i][j] = (ans.a[i][j] + m1.a[i][k] * m2.a[k][j]) % MOD;
            }
        }
    }
    return ans;
}

M mPow(M m, int k)
{
    M ans;
    for (int i = 0; i < 6; ++i)
    {
        for (int j = 0; j < 6; ++j)
        {
            if (i == j)
                ans.a[i][j] = 1;
            else
                ans.a[i][j] = 0;
        }
    }
    while (k)
    {
        if (k & 1)
        {
            ans = mMultiply(ans, m);
        }
        m = mMultiply(m, m);
        k >>= 1;
    }
    return ans;
}

int main()
{
    init();
    scanf("%d%d", &n, &m);
    M cMatrix;
    for (int i = 0; i < m; ++i)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        cMatrix.a[op[a] - 1][b - 1] = 0;
        cMatrix.a[op[b] - 1][a - 1] = 0;
    }

    M cMatrix_n_1 = mPow(cMatrix, n - 1);

    LL ans = 0;
    for (int j = 0; j < 6; ++j)
    {
        for (int i = 0; i < 6; ++i)
        {
            ans = (ans + cMatrix_n_1.a[i][j]) % MOD;
        }
    }

    LL t = 1;
    LL tmp = 4;
    LL p = n;
    while (p)
    {
        if (p & 1)
        {
            t = t * tmp % MOD;
        }
        tmp = tmp * tmp % MOD;
        p >>= 1;
    }
    printf("%lld", ans * t % MOD);

    return 0;
}