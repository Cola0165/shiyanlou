public class SingleNumber {
    public static int singleNumber(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(singleNumber(new int[]{4, 12, 34, 12, 4}));
        System.out.println(singleNumber(new int[]{4, 12, 34, 12, 4, 5, 34}));
    }
}