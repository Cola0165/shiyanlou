public class RadixSort {

  private static void radixSort(int[] nums) {
    int max = nums[0];
    // 指数，从个位到十位到百位...
    int exp;
    // 遍历得到最大值
    for (int num : nums) {
      if (num > max) {
        max = num;
      }
    }
    // 从个位开始，对数组每一位进行排序
    for (exp = 1; max / exp > 0; exp = exp * 10) {
      // 临时数组
      int[] tempNums = new int[nums.length];
      // 数值 0-9，桶的个数固定为 10
      int[] buckets = new int[10];
      // buckets 中存储的其实是数据出现的次数
      for (int value : nums) {
        buckets[(value / exp) % 10]++;
      }
      // 每一个值等于前面的元素次数加上自身（类似计数排序）
      for (int i = 1; i < 10; i++) {
        buckets[i] += buckets[i - 1];
      }
      // 从后往前遍历，将元素写会临时数组
      for (int i = nums.length - 1; i >= 0; i--) {
        tempNums[buckets[(nums[i] / exp) % 10] - 1] = nums[i];
        buckets[(nums[i] / exp) % 10]--;
      }
      // 将有序元素 tempNums 赋给 nums
      System.arraycopy(tempNums, 0, nums, 0, nums.length);
      printf(nums);
    }
  }
  public static void main(String[] args) {
    int[] nums = new int[]{98, 90, 34, 56, 21, 11, 43, 61, 39};
    printf(nums);
    radixSort(nums);
}
}