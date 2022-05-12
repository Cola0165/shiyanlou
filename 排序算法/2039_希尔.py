class Solution:
    def shellSort(self, nums):
        times = 1
        gap = len(nums) // 2
        while gap > 0:
            # print(
                # "第", times, "轮希尔排序, gap= ", gap, " ,结果：", end="")
            times += 1
            for i in range(gap, len(nums)):
                j = i
                temp = nums[j]
                while j - gap >= 0 and temp > nums[j - gap]:
                    # 移动法
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = temp
            
            gap = gap // 2
        self.printNums(nums)

    def printNums(self, nums):
        for i in range(len(nums)):
            print("%d " % nums[i], end="\n")
        # print("")


if __name__ == '__main__':
    solution = Solution()
    n=input()
    arr = input()
    # nums = [98, 90, 34, 56, 21, 11, 43, 61]
    nums = [int(n) for n in arr.split()]
    # solution.printNums(nums)
    solution.shellSort(nums)