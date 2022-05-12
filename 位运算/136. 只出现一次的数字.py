class SingleNumber:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result

if __name__ == '__main__':
    singleNumber = SingleNumber()
    print(singleNumber.singleNumber([4, 12, 34, 12, 4]))
    print(singleNumber.singleNumber([4, 12, 34, 12, 4, 5, 34]))