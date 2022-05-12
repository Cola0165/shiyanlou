public class QuickSort {

    public static void quickSort(int[] nums) {
      quickSort(nums, 0, nums.length - 1);
    }
  
    public static void quickSort(int nums[], int left, int right) {
      System.out.println("[" + left + " , " + right + "]");
      if (left < right) {
        // 区间左边界是 i，右边界是 j，基准值是 standardNum
        int i = left, j = right, standardNum = nums[left];
        while (i < j) {
          // 从右向左找第一个小于 standardNum的数
          while (i < j && nums[j] >= standardNum) {
            j--;
          }
          System.out.print(
            "standardNum:" +
            standardNum +
            ", 第1个小于等于standardNum的数： " +
            nums[j]
          );
          if (i < j) {
            // nums[i]已经被保存到standardNum，将nums[j]写到左边
            nums[i] = nums[j];
            i++;
          }
          // 从左向右找第一个大于等于 standardNum 的数
          while (i < j && nums[i] < standardNum) {
            i++;
          }
          System.out.println(", 第1个大于等于standardNum的数： " + nums[i]);
          if (i < j) {
            // 将较大的数写到右边
            nums[j] = nums[i];
            j--;
          }
        }
        // 将基准值写到中间
        nums[i] = standardNum;
        printf(nums);
        quickSort(nums, left, i - 1);
        printf(nums);
        quickSort(nums, i + 1, right);
      }
    }
    public static void main(String[] args) {
        int[] nums = new int[]{61, 90, 34, 56, 21, 11, 43, 68};
        printf(nums);
        quickSort(nums);
    }
  }