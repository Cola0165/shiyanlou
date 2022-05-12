from operator import itemgetter


class Solution:
    def mergeSort(self, nums):
        self.sort(nums, 0, len(nums) - 1)

    def sort(self, nums, left, right):
        if left == right:
            return
        mid = left + (right - left) // 2
        # print("left:", left, " , right:", right)
        self.sort(nums, left, mid)
        self.sort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        tempNums = [0] * (right - left + 1)
        i = 0
        index1 = left
        index2 = mid + 1
        # 比较左右两部分的元素，哪个小，就把那个元素填入temp中
        while index1 <= mid and index2 <= right:
            # 左边的元素更小
            if nums[index1] < nums[index2]:
                tempNums[i] = nums[index1]
                i += 1
                index1 += 1
            else:
                # 右边的元素更小
                tempNums[i] = nums[index2]
                i += 1
                index2 += 1
        # 如果左边还有元素剩下，则全部合并过去
        while index1 <= mid:
            tempNums[i] = nums[index1]
            i += 1
            index1 += 1
        # 如果右边有元素剩下，则把右边元素合并过去
        while index2 <= right:
            tempNums[i] = nums[index2]
            i += 1
            index2 += 1
        # 把最后的排序结果复制到原数组中
        for i in range(0, len(tempNums)):
            nums[left + i] = tempNums[i]

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
    # number = [98, 90, 34, 56, 21, 11, 43, 61]
    number = [int(n) for n in arr.split()]
    solution.mergeSort(number)
    solution.printNums(number)