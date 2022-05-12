class OnceNums:
    def findNumsAppearOnce(self, array):
        nums = []
        # A和B异或的结果
        res = 0
        for val in array:
            res ^= val
        # temp保存了两个数最后一个不同的位
        temp = res & (-res)
        # 保存和最后一个不同的位异或的结果
        res1 = 0
        for val in array:
            # 不等于0说明可能是其中一个数，至少排除了另外一个数
            if (temp & val) != 0:
                res1 ^= val
        # 由于其他满足条件的数字都出现两次，所以结果肯定就是只出现一次的数
        nums.append(res1)
        # 求出另外一个数
        nums.append(res ^ res1)
        return nums

if __name__ == '__main__':
    onceNums = OnceNums()
    print(onceNums.findNumsAppearOnce([5, 7, 65, 12, 43, 65, 12, 5]))
