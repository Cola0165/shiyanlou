#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class ScoreLine {
public:
    int lowestScore(int n, int x, int y, vector<int> nums) {
        int results = 0;
        // 排序
        sort(nums.begin(), nums.end());
        if (x > n / 2 || y < n / 2 + n % 2) {
            // 找不出符合的分数线
            results = -1;
        } else {
            // 最多淘汰y个，假设淘汰最多，分数线最高，剩下人数最少
            int less = n - y;
            // 晋级的人数最小是less，要求必须最小是x，取两者最大
            less = max(less, x);
            // 假定分数线
            results = nums[less - 1];
            int i;
            // 往后找，找到最后一个同分的
            for (i = less; i < n; i++) {
                if (nums[i] != results) {
                    break;
                }
            }
            // 假设以该分数划线，晋级和淘汰人数是否符合条件
            if (n - i >= x && n - i <= y && i >= x && i <= y) {
                return results;
            } else {
                results = -1;
            }
        }
        return results;
    }
};

int main() {
    ScoreLine scoreLine;
    int n,x,y;
    cin >> n >> x >> y;
    vector<int> nums(n);
    for(int i=0;i<n;i++){
        cin >> nums[i];
    }
    cout << scoreLine.lowestScore(n, x, y, nums) << endl;
    // cout << scoreLine.lowestScore(6, 2, 3, {1, 2, 2, 3, 3, 3}) << endl;
}