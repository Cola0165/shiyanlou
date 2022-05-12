import java.util.Scanner;
public class BubbleSort {

    public static void bubbleSort(int[] nums) {
      int size = nums.length;
      // 每轮针对前面（size-i）个数进行排序
      for (int i = 0; i < size - 1; i++) {
        System.out.println("第" + (i + 1) + "轮交换开始");
        // 每一轮排序，从第 0 个元素，到 size-1-i 个元素
        for (int j = 0; j < size - 1 - i; j++) {
          // 对比相邻的两个元素
          if (nums[j] > nums[j + 1]) {
            // 元素交换。使得大的元素在后面
            int temp = nums[j + 1];
            nums[j + 1] = nums[j];
            nums[j] = temp;
          }
          
        }
      }
      printf(nums);
    }

    public static void printf(int[] nums) {
        for (int num : nums) {
            System.out.print(num + " ");
        }
        System.out.println("");
    }

    public static void main(String[ ] args) {
        int[] nums = new int [500005];
        int n;
        Scanner in=new Scanner(System.in);
        n=in.nextInt();
        for(int i=0;i<n;i++)
        {
            nums[i]=in.nextInt();
        }
        in.close();
        bubbleSort(nums);
    }
  }