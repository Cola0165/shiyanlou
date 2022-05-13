#include "iostream"

using namespace std;

#include "algorithm"
#include "vector"
#include "queue"
#include "set"
#include "map"
#include "string"
#include "stack"

class Solution {
private:
    // 定义以 i 为结尾的最长子串 的长度 ，即 最长子串数组
    // 例如 dp[1] 就是 以 s[1] 为结尾的最长子串 的长度
    vector<int> dp;
public:
    int lengthOfLongestSubstring(string s) {
        // 如果只有一个字符或为空，直接返回字符串长度即可
        if (s.length() <= 1) {
            return s.length();
        }
        // 初始化最长子串数组
        dp.resize(s.length());
        // 设置第一个节点的 最长子串数组 为 1 。边界
        dp[0] = 1;

        dealChen(s);

        // 获取所有的最长子串数组 中的最大值，就是整个字符串的最长子串数组
        int result = 1;
        for (int i = 1; i < dp.size(); ++i) {
            if (result < dp[i]) {
                result = dp[i];
            }
        }

        return result;
    }

    /**
     * 核心思路为：
     *        处理 s[i] 节点时，其需要比较的最大长度为 dp[i-1],这样可以节省时间
     * @param s
     */
    void dealChen(string s) {
        for (int i = 1; i < s.length(); ++i) {
            // 最小 的 最长子串长度，就是节点本身 所以初始值为 1
            int temp = 1;
            // s[i] 和左边要比较的节点的距离 初始化为 1
            int j = 1;
            // 注意处理边界 只有字符不同时才需要继续循环
            while (i - j >= 0 && j <= dp[i - 1] && s[i] != s[i - j]) {
                temp++;
                j++;
            }
            // 保存不同字符的个数
            dp[i] = temp;
        }
    }
};

int main() {

    string s = "pwwkew";
    Solution *pSolution = new Solution;
    int i = pSolution->lengthOfLongestSubstring(s);
    cout << i << endl;
    system("pause");
    return 0;
}

// class Solution
// {
// public:
//     int lengthOfLongestSubstring(string s)
//     {
//         map<char, int> hash;
//         int ans = 0;
//         int i = 0;
//         int j = 0;
//         int n = s.length();
//         while (i < n && j < n)
//         {
//             if (hash.find(s[j]) == hash.end())
//             {
//                 hash[s[j++]] = j;
//                 ans = max(ans, j - i);
//             }
//             else
//                 hash.erase(s[i++]);
//         }
//         return ans;
//     }
// };

// class Solution
// {
// public:
//     int lengthOfLongestSubstring(string s)
//     {
//         map<char, int> hash;
//         int ans = 0;
//         int n = s.size();
//         for (int i = 0, j = 0; j < n; j++)
//         {
//             if (hash.find(s[j]) != hash.end())
//                 i = max(hash.find(s[j])->second + 1, i);
//             ans = max(ans, j - i + 1);
//             hash[s[j]] = j;
//         }
//         return ans;
//     }
// };