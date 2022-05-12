class Solution:
    def lowestScore(self, n, x, y, nums):
        results = 0
        # 排序
        nums.sort()
        if x > n / 2 or y < n / 2 + n % 2:
            # 找不出符合的分数线
            results = -1
        else:
            # 最多淘汰y个，假设淘汰最多，分数线最高，剩下人数最少
            less = n - y
            # 晋级的人数最小是less，要求必须最小是x，取两者最大
            less = max(less, x)
            # 假定分数线
            results = nums[less - 1]

            # 往后找，找到最后一个同分的
            for i in range(less, n):
                if nums[i] != results:
                    break
            # 假设以该分数划线，晋级和淘汰人数是否符合条件
            if n - i >= x and n - i <= y and i >= x and i <= y:
                return results
            else:
                results = -1
        return results


if __name__ == '__main__':
    solution = Solution()
    n,x,y=map(int, input().split())
    arr = input()
    nums = [int(n) for n in arr.split()]
    print(solution.lowestScore(n, x, y, nums))
    # print(solution.lowestScore(6, 2, 3, [1, 2, 2, 3, 3, 3]))