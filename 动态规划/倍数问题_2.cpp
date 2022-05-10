#include <iostream>
#include <vector>
using namespace std;

int N, k;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> k;
    vector<vector<int> > vec(k, vector<int>(3, -1));
    for (int i = 0; i < N; ++i)
    {
        int temp;
        cin >> temp;
        int y = temp % k;
        if (temp > vec[y][0])
        {
            vec[y][2] = vec[y][1];
            vec[y][1] = vec[y][0];
            vec[y][0] = temp;
        }
        else if (temp > vec[y][1])
        {
            vec[y][2] = vec[y][1];
            vec[y][1] = temp;
        }
        else if (temp > vec[y][2])
            vec[y][2] = temp;
    }

    vector<int> ans(3);
    int result = 0;
    for (int i = 0; i < k; ++i)
        for (int j = i; j < k; ++j)
        {
            int r = (k - i + k - j) % k;
            ans[0] = vec[i][0];
            if (i == j)
            {
                ans[1] = vec[i][1];
                if (r == i)
                    ans[2] = vec[i][2];
                else
                    ans[2] = vec[r][0];
            }
            else
            {
                ans[1] = vec[j][0];
                if (r == i)
                    ans[2] = vec[i][1];
                else if (r == j)
                    ans[2] = vec[j][1];
                else
                    ans[2] = vec[r][0];
            }
            if (ans[0] != -1 && ans[1] != -1 && ans[2] != -1 && ans[1] + ans[2] + ans[0] > result)
                result = ans[1] + ans[2] + ans[0];
        }
    cout << result;
}