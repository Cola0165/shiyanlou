#include <stdio.h>
int DP[1011][1011];
int main()
{
    int i, j;
    DP[1][0] = 1;
    for (i = 1; i <= 1010; i++)
        DP[i][0] = 1;
    for (i = 1; i <= 1010; i++)
    {
        for (j = 1; j <= i; j++)
        {
            if (i == j)
                DP[i][j] = DP[i][j - 1];
            else
                /*__________________*/DP[i][j] = (DP[i - 1][j] + DP[i][j - 1]) % 2020;
        }
    }
    printf("%d", DP[1010][1010]);
    return 0;
}