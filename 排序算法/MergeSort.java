public class MergeSort {

    public static void mergeSort(int[] nums) {
      sort(nums, 0, nums.length - 1);
    }
  
    public static void sort(int[] nums, int left, int right) {
      if (left == right) {
        return;
      }
      int mid = left + ((right - left) / 2);
      System.out.println("left:" + left + " , right:" + right);
      sort(nums, left, mid);
      sort(nums, mid + 1, right);
      merge(nums, left, mid, right);
      printf(nums);
    }
  
    public static void merge(int[] nums, int left, int mid, int right) {
      // 申请临时数组
      int[] tempNums = new int[right - left + 1];
      int i = 0;
      int index1 = left;
      int index2 = mid + 1;
      // 比较左右两部分的元素，哪个小，就把那个元素填入temp中
      while (index1 <= mid && index2 <= right) {
        // 左边的元素更小
        if (nums[index1] < nums[index2]) {
          tempNums[i] = nums[index1];
          i++;
          index1++;
        } else {
          // 右边的元素更小
          tempNums[i] = nums[index2];
          i++;
          index2++;
        }
      }
      // 如果左边还有元素剩下，则全部合并过去
      while (index1 <= mid) {
        tempNums[i] = nums[index1];
        i++;
        index1++;
      }
      // 如果右边有元素剩下，则把右边元素合并过去
      while (index2 <= right) {
        tempNums[i] = nums[index2];
        i++;
        index2++;
      }
      // 把最后的排序结果复制到原数组中
      for (i = 0; i < tempNums.length; i++) {
        nums[left + i] = tempNums[i];
      }
    }
    public static void main(String[] args) {
        int[] nums = new int[]{98, 90, 34, 56, 21, 11, 43, 61};
        printf(nums);
        mergeSort(nums);
        printf(nums);
        }
  }