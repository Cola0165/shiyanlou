class Solution:
    def radixSort(self, nums):
        max = nums[0]
        # 指数，从个位到十位到百位...
        exp = 1
        # 遍历得到最大值
        for num in nums:
            if num > max:
                max = num
        # 从个位开始，对数组每一位进行排序
        while max // exp > 0:
            # 临时数组
            tempNums = [0] * (len(nums))
            # 数值 0-9，桶的个数固定为 10
            buckets = [0] * 10
            # buckets 中存储的其实是数据出现的次数
            for value in nums:
                buckets[(value // exp) % 10] += 1
            # 每一个值等于前面的元素次数加上自身（类似计数排序）
            for i in range(1, 10):
                buckets[i] += buckets[i - 1]
            # 从后往前遍历，将元素写会临时数组
            for i in range(len(nums) - 1, -1, -1):
                tempNums[buckets[(nums[i] // exp) % 10] - 1] = nums[i]
                buckets[(nums[i] // exp) % 10] -= 1
            # 将有序元素 tempNums 赋给 nums
            nums = tempNums
            # self.printNums(nums)
            exp = exp * 10

        return tempNums

    def printNums(self, nums):
        for i in range(len(nums)):
            print("%d " % nums[i], end="")
        print()
        for i in range(len(nums)-1,-1,-1):
            print("%d " % nums[i], end="")
        # print("")


if __name__ == '__main__':
    solution = Solution()
    n=input()
    arr = input()
    # numbers = [98, 90, 34, 56, 21, 11, 43, 61, 39]
    numbers = [int(n) for n in arr.split()]
    numbers = solution.radixSort(numbers)
    solution.printNums(numbers)