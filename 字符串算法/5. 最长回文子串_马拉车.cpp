#include <iostream>
#include <string>

using namespace std;

string preProcess(string &s);

string longestPalindrome(string &str);


int main() {
    string str = "abdbdc";
    cout << longestPalindrome(str) << endl;
    return 0;
}

// 构造字符串
string preProcess(string &s) {
    int n = s.length();
    if (n == 0) {
        return "^$";
    }
    string ret = "^";
    for (int i = 0; i < n; i++)
        ret = ret + "#" + s[i];
    ret = ret + "#$";
    return ret;
}

// 马拉车算法
string longestPalindrome(string &str) {
    string S = preProcess(str);
    int n = S.length();
    // 保存回文串的长度
    int P[n];
    // 保存边界最右的回文中心以及右边界
    int center = 0, right = 0;
    // 从第 1 个字符开始
    for (int i = 1; i < n - 1; i++) {
        // 找出i关于前面中心的对称
        int mirror = 2 * center - i;
        if (right > i) {
            // i 在右边界的范围内，看看i的对称点的回文串长度，以及i到右边界的长度，取两个较小的那个
            // 不能溢出之前的边界，否则就得中心拓展
            P[i] = min(right - i, P[mirror]);
        } else {
            // 超过范围了，中心拓展
            P[i] = 0;
        }

        // 中心拓展
        while (S[i + 1 + P[i]] == S[i - 1 - P[i]]) {
            P[i]++;
        }

        // 看看新的索引是不是比之前保存的最右边界的回文串还要靠右
        if (i + P[i] > right) {
            // 更新中心
            center = i;
            // 更新右边界
            right = i + P[i];
        }

    }

    // 通过回文长度数组找出最长的回文串
    int maxLen = 0;
    int centerIndex = 0;
    for (int i = 1; i < n - 1; i++) {
        if (P[i] > maxLen) {
            maxLen = P[i];
            centerIndex = i;
        }
    }
    int start = (centerIndex - maxLen) / 2;
    return str.substr(start, maxLen);
}