public class InsertionSort {

    public static void insertionSort(int[] nums) {
      if (nums == null) {
        return;
      }
      int size = nums.length;
      int index, temp;
      for (int i = 1; i < size; i++) {
        // 当前选择插入的元素前面一个索引值
        index = i - 1;
        // 当前需要插入的元素
        temp = nums[i];
        while (index >= 0 && nums[index] > temp) {
          nums[index + 1] = nums[index];
          index--;
        }
        // 插入空出来的位置
        nums[index + 1] = temp;
        System.out.print("第" + (i) + "轮插入结果：");
        printf(nums);
      }
    }
    public static void main(String[] args) {
        int[]nums = new int[]{98,90,34,56,21};
        printf(nums);
        insertionSort(nums);
    }
  }