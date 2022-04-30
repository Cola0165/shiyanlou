a = [1, 2, 3]
b = [3, 4, 5]


def permutation(s, nums, p, q):
    if p == q:
        s.append(list(nums))
    else:
        for i in range(p, q):
            nums[i], nums[p] = nums[p], nums[i]
            permutation(s, nums, p+1, q)
            nums[i], nums[p] = nums[p], nums[i]


if __name__ == '__main__':
    all_a = []
    permutation(all_a, a, 0, len(a))

    all_b = []
    permutation(all_b, b, 0, len(b))

    z = list(zip(all_a, all_b))
    print(z)