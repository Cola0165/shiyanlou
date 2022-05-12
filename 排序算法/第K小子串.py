import heapq
class Compare:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        """
        重写比较器，类似于Java中的compare，让其从小到大排序
        """
        return self.value > other.value


class Solution:
    def getKSortStr(self, str,k):
        mySet = set()
        # 优先队列
        pq = []
        for strLen in range(1,k+1):
            for i in range(0, len(str) - strLen + 1):
                substr = str[i:i+ strLen]
                if substr not in mySet:
                    heapq.heappush(pq,Compare(substr))
                    if len(pq) > k:
                        heapq.heappop(pq).value
                mySet.add(substr)
        return pq[0].value

if __name__ == '__main__':
    solution = Solution()
    s=input()
    k=int(input())
    print(solution.getKSortStr(s,k))