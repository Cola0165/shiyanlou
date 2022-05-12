public class OnceNums {
    public static void main(String[] args) {
        int nums[] = new int[]{5, 7, 65, 12, 43, 65, 12, 5};
        int results[] = findNumsAppearOnce(nums);
        System.out.println(results[0] + " " + results[1]);
    }

    public static int[] findNumsAppearOnce(int[] array) {
        int[] nums = new int[2];
        // A和B异或的结果
        int res = 0;
        for (int val : array) {
            res ^= val;
        }
        // temp保存了两个数最后一个不同的位
        int temp = res & (-res);

        // 保存和最后一个不同的位异或的结果
        int res1 = 0;
        for (int val : array) {
            // 不等于0说明可能是其中一个数，至少排除了另外一个数
            if ((temp & val) != 0) {
                res1 ^= val;
            }
        }
        // 由于其他满足条件的数字都出现两次，所以结果肯定就是只出现一次的数
        nums[0] = res1;
        // 求出另外一个数
        nums[1] = res ^ res1;
        return nums;
    }
}