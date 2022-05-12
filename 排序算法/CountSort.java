public class CountSort {

    public static void countSort(int[] nums) {
      int max = nums[0];
      int min = nums[0];
      for (int i = 1; i < nums.length; i++) {
        if (nums[i] > max) {
          max = nums[i];
        }
        if (nums[i] < min) {
          min = nums[i];
        }
      }
      System.out.println("min:" + min + ",max:" + max);
      int count = max - min;
      int[] countNums = new int[count + 1];
      for (int i = 0; i < nums.length; i++) {
        countNums[nums[i] - min]++;
      }
      System.out.print("countNums: ");
      printf(countNums);
      int sum = 0;
      // 后面的元素等于前面元素加上自身
      for (int i = 0; i < count + 1; i++) {
        sum += countNums[i];
        countNums[i] = sum;
      }
      System.out.print("countNums: ");
      printf(countNums);
      int[] newNums = new int[nums.length];
      for (int i = nums.length - 1; i >= 0; i--) {
        /**
         * nums[i] - min 表示原数组 nums 里面第i位置对应的数在统计数组里面的位置索引
         */
        newNums[countNums[nums[i] - min] - 1] = nums[i];
        countNums[nums[i] - min]--;
      }
      printf(newNums);
    }
    public static void main(String[] args) {
        int[] nums = new int[]{11, 9, 11, 13, 19, 14, 16, 14, 8, 17};
        printf(nums);
        countSort(nums);
    }
  }