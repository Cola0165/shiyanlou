class Solution:
    def selectionSort(self, nums):
        times = 0
        size = len(nums)
        minIndex, temp = 0, 0

        for i in range(size - 1):
            # print("第", (i + 1), "轮选择开始：")
            minIndex = i
            for j in range(i + 1, size):
                times = times + 1
                if (nums[j] > nums[minIndex]):
                    minIndex = j
            # print("交换 ", nums[i], "和", nums[minIndex])
            print(end="")
            temp = nums[i]
            nums[i] = nums[minIndex]
            nums[minIndex] = temp
        self.printNums(nums)
        # print("比较次数：", times, end="")

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
    solution.selectionSort(nums)