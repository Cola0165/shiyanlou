import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n,x,y;
        Scanner scan = new Scanner(System.in);
        n=scan.nextInt();
        x=scan.nextInt();
        y=scan.nextInt();
        int []nums = new int[n];
        for(int i=0;i<n;i++) {
            nums[i]=scan.nextInt();
        }
        scan.close();
        System.out.println(lowestScore(n, x, y, nums));
        // System.out.println(lowestScore(6, 2, 3, new int[]{1, 2, 2, 3, 3, 3}));
    }

    public static int lowestScore(int n, int x, int y, int[] nums) {
        int results = 0;
        // 排序
        Arrays.sort(nums);
        if (x > n / 2 || y < n / 2 + n % 2) {
            // 找不出符合的分数线
            results = -1;
        } else {
            // 最多淘汰y个，假设淘汰最多，分数线最高，剩下人数最少
            int less = n - y;
            // 晋级的人数最小是less，要求必须最小是x，取两者最大
            less = Math.max(less, x);
            // 假定分数线
            results = nums[less - 1];
            int i;
            // 往后找，找到最后一个同分的
            for (i = less; i < n; i++) {
                if (nums[i] != results) {
                    break;
                }
            }
            // 假设以该分数划线，晋级和淘汰人数是否符合条件
            if (n - i >= x && n - i <= y && i >= x && i <= y) {
                return results;
            } else {
                results = -1;
            }
        }
        return results;
    }

}