public class ShellSort {
    public static void shellSort(int[] nums) {
        int times = 1;
        for (int gap = nums.length / 2; gap > 0; gap /= 2) {
            System.out.print(
                    "第" + (times++) + "轮希尔排序, gap= " + gap + " ,结果："
            );
            for (int i = gap; i < nums.length; i++) {
                int j = i;
                int temp = nums[j];
                while (j - gap >= 0 && temp < nums[j - gap]) {
                    // 移动法
                    nums[j] = nums[j - gap];
                    j -= gap;
                }
                nums[j] = temp;
            }
            printf(nums);
        }
    }
    public static void main(String[] args) {
        int[] nums = new int[]{98, 90, 34, 56, 21, 11, 43, 61};
        printf(nums);
        shellSort(nums);
    }
}