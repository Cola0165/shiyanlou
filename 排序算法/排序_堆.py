class Solution:
    def heapSort(self, nums):
        # 首先需要构建最大堆
        i = len(nums) // 2 - 1
        while i >= 0:
            # 从第一个非叶子结点调整结构，大的往上走
            self.adjustHeap(nums, i, len(nums))
            i = i - 1
        # self.printNums(nums)
        # print("-----------------------------");
        # 交换元素和调整
        for j in range(len(nums) - 1, 0, -1):
            # 将堆顶元素与末尾元素交换
            self.swap(nums, 0, j)
            # 重新调整，大的元素往上交换
            self.adjustHeap(nums, 0, j);
            # self.printNums(nums);
            # print("-----------------------------");

    def adjustHeap(self, nums, i, length):
        temp = nums[i]
        # 从左节点开始
        k = i * 2 + 1
        while k < length:
            # 如果右节点更大，那么指向右节点
            if k + 1 < length and nums[k] < nums[k + 1]:
                k = k + 1
            # 子节点的值直接给父节点
            if nums[k] > temp:
                nums[i] = nums[k]
                i = k
            else:
                break
            k = 2 * k + 1
        # self.printNums(nums)
        # 最后将最上面的节点置，放到当前的节点
        nums[i] = temp

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

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
    # numbers = [98, 90, 34, 56, 21, 11, 43, 61]
    numbers = [int(n) for n in arr.split()]
    solution.heapSort(numbers)
    solution.printNums(numbers)