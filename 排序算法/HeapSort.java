public class HeapSort {

    public static void heapSort(int[] nums) {
      // 首先需要构建最大堆
      for (int i = nums.length / 2 - 1; i >= 0; i--) {
        // 从第一个非叶子结点调整结构，大的往上走
        adjustHeap(nums, i, nums.length);
      }
      printf(nums);
      System.out.println("-----------------------------");
      // 交换元素和调整
      for (int j = nums.length - 1; j > 0; j--) {
        // 将堆顶元素与末尾元素交换
        swap(nums, 0, j);
        // 重新调整，大的元素往上交换
        adjustHeap(nums, 0, j);
        printf(nums);
        System.out.println("-----------------------------");
      }
    }
  
    /**
     * 调整大顶堆
     */
    public static void adjustHeap(int[] nums, int i, int length) {
      // 取出当前元素
      int temp = nums[i];
      //从左节点开始
      for (int k = i * 2 + 1; k < length; k = k * 2 + 1) {
        // 如果右节点更大，那么指向右节点
        if (k + 1 < length && nums[k] < nums[k + 1]) {
          k++;
        }
        // 子节点的值直接给父节点
        if (nums[k] > temp) {
          nums[i] = nums[k];
          i = k;
        } else {
          break;
        }
        printf(nums);
      }
      // 最后将最上面的节点置，放到当前的节点
      nums[i] = temp;
    }
  
    /**
     * 交换元素
     */
    public static void swap(int[] nums, int a, int b) {
      int temp = nums[a];
      nums[a] = nums[b];
      nums[b] = temp;
    }
  
    public static void printf(int[] nums) {
      for (int num : nums) {
        System.out.print(num + " ");
      }
      System.out.println("");
    }
    public static void main(String[] args) {
        int[] nums = new int[]{98, 90, 34, 56, 21, 11, 43, 61};
        printf(nums);
        heapSort(nums);
        printf(nums);
    }
  }