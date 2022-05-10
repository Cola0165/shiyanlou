#include <iostream>
using namespace std;
int num[5][1010] = {0};

int dp(int k, int n)
{
    int res = 10000;
    if (n == 0)
        return 0;
    if (k == 1)
        return n;
    if (num[k][n])
        return num[k][n];
    for (int i = 1; i <= n; i++)
    {
        /*__________________*/res = min(res, max(dp(k - 1, i - 1), dp(k, n - i)) + 1);
    }
    num[k][n] = res;
    return res;
}

int main()
{
    cout << dp(3, 1000) << endl;
    return 0;
}