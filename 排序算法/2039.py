class Solution:
    def bubbleSort(self, nums):
        size = len(nums)
        # 每轮针对前面（size - i）个数进行排序
        for i in range(size):
            # print("第", (i + 1), "轮交换开始")
            for j in range(0, size - 1 - i):
                if nums[j] < nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        self.printNums(nums)

    def printNums(self, nums):
        for i in range(len(nums)):
            print("%d " % nums[i], end="\n")
        # print("")


if __name__ == '__main__':
    solution = Solution()
    n=input()
    arr = input()
    # nums = [98, 90, 34, 56, 21]
    nums = [int(n) for n in arr.split()]
    # solution.printNums(nums)
    solution.bubbleSort(nums)