#include <iostream>
#include <cstring>

using namespace std;

const int N = 55, M = 15;
const int mod = 1e9 + 7;
int n,m,k;
// f[i][j][nn][mm]  i,j 时 有nn个物品，且最大价值为mm 的方案数
int f[N][N][M][M];  
int t[N][N];

int main() {
    cin >> n >> m >> k;
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= m; j++) {
            cin >> t[i][j];
            t[i][j] ++;     // 对于一个物品，不选的话，他带来的价值为0。而原本价值的范围为0-12，这样就可以变成1-13
        }
    
    f[1][1][0][0] = 1;              // 不选 1,1 的物品
    f[1][1][1][t[1][1]] = 1;    // 选1,1 的物品
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= m; j++)
            for(int nn = 0; nn <= k; nn++)
                for(int mm = 0; mm < M; mm++) {
                    // 不取 i,j
                    f[i][j][nn][mm] = ((f[i][j][nn][mm] + f[i-1][j][nn][mm]) % mod + f[i][j-1][nn][mm]) % mod;
                    
                    // 取i,j  得保证当前状态的最大价值为 mm
                    if(nn > 0 && mm == t[i][j]) {
                        // 从之前的最大值 0 - mm 变迁
                        for(int s = 0; s < mm; s++)
                            f[i][j][nn][mm] = ((f[i][j][nn][mm] + f[i-1][j][nn-1][s]) % mod + f[i][j-1][nn-1][s]) % mod;
                    }
                }
    
    int ans = 0;
    for(int i = 1; i <= 13; i++) ans = (ans + f[n][m][k][i]) % mod;
    cout << ans;
    return 0;
}