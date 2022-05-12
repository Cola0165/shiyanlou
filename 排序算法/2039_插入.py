class Solution:
    def insertionSort(self, nums):
        if len(nums) == 0:
            return
        size = len(nums)
        index, temp = 0, 0
        for i in range(1, size):
            # 当前选择插入的元素前面一个索引值
            index = i - 1
            # 当前需要插入的元素
            temp = nums[i]
            while index >= 0 and nums[index] < temp:
                nums[index + 1] = nums[index]
                index = index - 1
            # 插入空出来的位置
            nums[index + 1] = temp
            # print("第 %d 轮插入结果：" %i)
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
    solution.insertionSort(nums)