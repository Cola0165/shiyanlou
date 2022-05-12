class Solution:

    def findLongestPalindrome(self, str):
        if str == None or len(str) < 2:
            return str
        maxLen = 1
        result = str[0:1]
        for i in range(0, len(str) - 1):
            # 中心为i的奇数个回文串
            odd = self.spread(str, i, i)
            # 中心为i和i + 1 的偶数个回文串
            even = self.spread(str, i, i + 1)
            # 先比较出两者最长的
            maxValue = odd if len(odd) > len(even) else even;
            # 与之前记录的最长回文串比较
            if len(maxValue) > maxLen:
                # 更新最长串
                maxLen = len(maxValue);
                result = maxValue;
        return result

    def spread(self, str, left, right):
        size = len(str)
        while left >= 0 and right < size:
            if str[left] == str[right]:
                left -= 1
                right += 1
            else:
                break
        return str[left + 1:right]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLongestPalindrome("abdbdc"))