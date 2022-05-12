import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BucketSort {

  public static void bucketSort(int[] nums) {
    // 遍历数组获取最大最小值
    int max = Integer.MIN_VALUE;
    int min = Integer.MAX_VALUE;
    for (int i = 0; i < nums.length; i++) {
      max = Math.max(max, nums[i]);
      min = Math.min(min, nums[i]);
    }

    // 计算桶的数量
    int bucketNum = (max - min) / nums.length + 1;
    System.out.println(
      "最小：" + min + "，最大：" + max + ",桶的数量：" + bucketNum
    );
    List<List<Integer>> buckets = new ArrayList<List<Integer>>(bucketNum);
    for (int i = 0; i < bucketNum; i++) {
      buckets.add(new ArrayList<Integer>());
    }

    // 将每个元素放入桶
    for (int i = 0; i < nums.length; i++) {
      int num = (nums[i] - min) / (nums.length);
      buckets.get(num).add(nums[i]);
    }

    // 对每个桶内部进行排序
    for (int i = 0; i < buckets.size(); i++) {
      Collections.sort(buckets.get(i));
    }

    // 将桶的元素复制到数组中
    int index = 0;
    for (int i = 0; i < buckets.size(); i++) {
      for (int j = 0; j < buckets.get(i).size(); j++) {
        nums[index++] = buckets.get(i).get(j);
      }
    }
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
    bucketSort(nums);
    printf(nums);
}
}