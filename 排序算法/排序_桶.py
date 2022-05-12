class Solution:
    def bucketSort(self, nums):
        maxValue = max(nums)
        minValue = min(nums)
        bucketNum = (maxValue - minValue) // len(nums) + 1
        # print("最小：", minValue, "，最大：", maxValue, ",桶的数量：", bucketNum)
        buckets = [[] for _ in range(bucketNum)]
        for i in range(0, len(nums)):
            num = (nums[i] - minValue) // len(nums)
            buckets[num].append(nums[i])
        for i in range(bucketNum):
            buckets[i].sort()
        index = 0
        for i in range(bucketNum):
            for j in range(len(buckets[i])):
                nums[index] = buckets[i][j]
                index += 1
        self.printNums(nums)

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
    solution.bucketSort(number)