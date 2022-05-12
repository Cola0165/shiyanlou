#include <iostream>
#include <vector>

using namespace std;

class OnceNums {
public:
    vector<int> findNumsAppearOnce(vector<int> &array) {
        vector<int> results;
        // A和B异或的结果
        int res = 0;
        for (int val : array) {
            res ^= val;
        }
        // temp保存了两个数最后一个不同的位
        int temp = res & (-res);
        // 保存和最后一个不同的位异或的结果
        int res1 = 0;
        for (int val : array) {
            // 不等于0说明可能是其中一个数，至少排除了另外一个数
            if ((temp & val) != 0) {
                res1 ^= val;
            }
        }
        // 由于其他满足条件的数字都出现两次，所以结果肯定就是只出现一次的数

        int res2 = res ^res1;
        if (res1 < res2) {
            results.push_back(res1);
            results.push_back(res2);
        } else {
            results.push_back(res2);
            results.push_back(res1);
        }
        return results;
    }
};

int main() {
    OnceNums onceNums;
    vector<int> nums = {5, 7, 65, 12, 43, 65, 12, 5};
    vector<int> results = onceNums.findNumsAppearOnce(nums);
    cout << results[0] << "  " << results[1] << endl;
}