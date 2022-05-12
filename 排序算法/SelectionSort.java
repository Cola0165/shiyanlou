public class SelectionSort {

    public static void selectionSort(int[] nums) {
      int times = 0;
      int size = nums.length;
      int minIndex, temp;
      for (int i = 0; i < size - 1; i++) {
        System.out.print("第" + (i + 1) + "轮选择开始：");
        minIndex = i;
        for (int j = i + 1; j < size; j++) {
          times++;
          if (nums[j] < nums[minIndex]) {
            minIndex = j;
          }
        }
        System.out.println("交换 " + nums[i] + "和" + nums[minIndex]);
        temp = nums[i];
        nums[i] = nums[minIndex];
        nums[minIndex] = temp;
        printf(nums);
      }
      System.out.println("比较次数：" + times);
    }

    public static void main(String[] args) {
        int[]nums = new int[]{98,90,34,56,21};
        printf(nums);
        selectionSort(new int[]{98,90,34,56,21});
    }
  }