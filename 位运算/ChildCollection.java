import java.util.ArrayList;
import java.util.List;

public class ChildCollection {
    public static void main(String[] args) {
        int nums[] = {1,2,3};
        List<List<Integer>> results = findChildCollection(nums);
        System.out.println(results.toString());
    }

    public static List<List<Integer>> findChildCollection(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        for (int i = 0; i < (1 << nums.length); i++) {
            List<Integer> subResult = new ArrayList<>();
            for (int k = 0; k < nums.length; k++)
                if (((i >> k) & 1) == 1) {
                    subResult.add(nums[k]);
                }
            results.add(subResult);
        }
        return results;
    }
}