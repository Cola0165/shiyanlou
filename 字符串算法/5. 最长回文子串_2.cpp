#include <iostream>
#include <string>
using namespace std;

string findLongestPalindrome(string &str);
string spread(string &str, int left, int right);

int main() {
    string str = "acbacabbc";
    cout<<findLongestPalindrome(str)<<endl;
    return 0;
}

string findLongestPalindrome(string &str) {
  if (str.size() < 2) {
    return str;
  }
  int maxLen = 1;
    string result = str.substr(0, 1);
  for (int i = 0; i < str.size() - 1; i++) {
    // 中心为 i 的奇数个回文串
      string odd = spread(str, i, i);
    // 中心为 i 和 i+1 的偶数个回文串
      string even = spread(str, i, i + 1);
    // 先比较出两者最长的
      string max = odd.size() > even.size() ? odd : even;
    // 与之前记录的最长回文串比较
    if (max.size() > maxLen) {
      // 更新最长串
      maxLen = max.size();
      result = max;
    }
  }
  return result;
}

string spread(string &str, int left, int right) {
  int len = str.size();
  while (left >= 0 && right < len) {
    if (str[left] == str[right]) {
      left--;
      right++;
    } else {
      break;
    }
  }
  return str.substr(left + 1, right-left-1);
}