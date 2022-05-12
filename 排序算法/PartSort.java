import java.util.Arrays;

public class PartSort {
    public static void main(String[] args) {
        int array[] = {11, 34, 56, 45, 40, 60, 70, 89};
        int results[] = partSort(array);
        System.out.println("待排序区间：[ " + results[0] + " , " + results[1] + " ]");
    }

    public static int[] partSort(int[] array) {
        int[] sortedArray = array.clone();
        int[] results = new int[]{-1, -1};
        Arrays.sort(sortedArray);
        int len = sortedArray.length;
        // 从左到右找不同
        for (int i = 0; i < len; ++i)
            if (sortedArray[i] != array[i]) {
                results[0] = i;
                break;
            }
        if (results[0] < 0) return results;
        // 从右到左找不同
        for (int i = len - 1; i > -1; --i)
            if (sortedArray[i] != array[i]) {
                results[1] = i;
                break;
            }
        return results;
    }
}