class Solution:

    def longestPalindrome(self, str):
        result = ""
        maxValue = 0
        size = len(str)
        for i in range(0, size):
            for j in range(1, size + 1):
                # 判断每一段子串
                temp = str[i:j]
                if self.isMatch(temp) and len(temp) > maxValue:
                    result = str[i:j]
                    maxValue = max(maxValue, len(result))
        return result

    def isMatch(self, str):
        size = len(str)
        for i in range(0, size // 2):
            if str[i] != str[size - i - 1]:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("abdbdc"))