class Solution:
    def countSort(self, nums):
        max = nums[0]
        min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > max:
                max = nums[i]
            if nums[i] < min:
                min = nums[i]
        # print("min:", min, ",max:", max)
        count = max - min
        countNums = [0] * (count + 1)
        for i in range(0, len(nums)):
            countNums[nums[i] - min] += 1
        # print("countNums: ", end="")
        # self.printNums(countNums)
        sum = 0
        # 后面的元素等于前面元素加上自身
        for i in range(0, count + 1):
            sum += countNums[i]
            countNums[i] = sum
        # print("countNums: ", end="")
        # self.printNums(countNums)
        newNums = [0] * (len(nums))
        i = len(nums) - 1
        while i >= 0:
            # nums[i] - min 表示原数组 nums 里面第i位置对应的数在统计数组里面的位置索引
            newNums[countNums[nums[i] - min] - 1] = nums[i]
            countNums[nums[i] - min] -= 1
            i -= 1
        self.printNums(newNums)

    def printNums(self, nums):
        for i in range(len(nums)-1,-1,-1):
            print("%d" % nums[i], end="\n")
        # print("")


if __name__ == '__main__':
    solution = Solution()
    n=input()
    arr = input()
    # number = [11, 9, 11, 13, 19, 14, 16, 14, 8, 17]
    number = [int(n) for n in arr.split()]
    solution.countSort(number)