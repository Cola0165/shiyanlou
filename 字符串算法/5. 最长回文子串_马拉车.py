class Manacher:
    # 构造字符串
    def preProcess(self, s):
        n = len(s)
        if n == 0:
            return "^$"
        ret = "^"
        for i in range(0, n):
            ret = ret + "#" + s[i]
        ret = ret + "#$"
        return ret

    # 马拉车算法
    def longestPalindrome(self, str):
        S = self.preProcess(str)
        n = len(S)
        # 保存回文串的长度
        P = [0] * n
        # 保存边界最右的回文中心以及右边界
        center = 0
        right = 0
        # 从第 1 个字符开始
        for i in range(1, n - 1):
            # 找出i关于前面中心的对称
            mirror = 2 * center - i
            if right > i:
                # i 在右边界的范围内，看看i的对称点的回文串长度，以及i到右边界的长度，取两个较小的那个
                # 不能溢出之前的边界，否则就得中心拓展
                P[i] = min(right - i, P[mirror])
            else:
                # 超过范围了，中心拓展
                P[i] = 0
            # 中心拓展
            while S[i + 1 + P[i]] == S[i - 1 - P[i]]:
                P[i] = P[i] + 1
            # 看看新的索引是不是比之前保存的最右边界的回文串还要靠右
            if i + P[i] > right:
                # 更新中心
                center = i
                # 更新右边界
                right = i + P[i]
        # 通过回文长度数组找出最长的回文串
        maxLen = 0
        centerIndex = 0
        for i in range(1, n - 1):
            if P[i] > maxLen:
                maxLen = P[i]
                centerIndex = i
        start = (centerIndex - maxLen) // 2
        return str[start : start+maxLen]


if __name__ == '__main__':
    manacher = Manacher()
    # bdb
    print(manacher.longestPalindrome("abdbdc"))
    # bacab
    print(manacher.longestPalindrome("acbacabbc"))