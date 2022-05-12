class Solution:
    def quickSort(self, nums):
        self.sort(nums, 0, len(nums) - 1)

    def sort(self, nums, left, right):
        # print("[", left, " , ", right, "]")
        if left < right:
            i = left
            j = right
            standardNum = nums[left]
            while i < j:
                while i < j and nums[j] >= standardNum:
                    j -= 1
                # print("standardNum:", standardNum, ", 第1个小于等于standardNum的数： ", nums[j], end="")
                if i < j:
                    # nums[i]已经被保存到standardNum，将nums[j]写到左边
                    nums[i] = nums[j];
                    i += 1
                while i < j and nums[i] < standardNum:
                    i += 1
                # print(", 第1个大于等于standardNum的数： ", nums[i])
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            nums[i] = standardNum
            # self.printNums(nums);
            self.sort(nums, left, i - 1)

            self.sort(nums, i + 1, right)

    def printNums(self, nums):
        for i in range(len(nums)-1,-1,-1):
            print("%d" % nums[i], end="\n")
        # print("")


if __name__ == '__main__':
    solution = Solution()
    n=input()
    arr = input()
    # nums = [61, 90, 34, 56, 21, 11, 43, 68]
    nums = [int(n) for n in arr.split()]
    # solution.printNums(nums)
    solution.quickSort(nums)
    solution.printNums(nums)