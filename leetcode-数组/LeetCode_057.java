public class LeetCode_057 {
    public static int[][] insert(int[][] intervals, int[] newInterval) {
        if (intervals == null || intervals.length == 0) {
            return new int[][]{newInterval};
        }
        int length = intervals.length;
        if (newInterval[1] < intervals[0][0]) {
            // 如果新区间的最大值小于所有区间的最小值，则不需要合并，将新区间放在intervals的最前面
            int[][] newIntervals = new int[length + 1][2];
            newIntervals[0] = newInterval;
            for (int i = 0; i < length; i++) {
                newIntervals[i + 1] = intervals[i];
            }
            return newIntervals;
        } else if (newInterval[0] > intervals[length - 1][1]) {
            // 如果新区间的最小值大于所有区间的最大值，则不需要合并，将新区间放在intervals的最后面
            int[][] newIntervals = new int[length + 1][2];
            for (int i = 0; i < length; i++) {
                newIntervals[i] = intervals[i];
            }
            newIntervals[length] = newInterval;
            return newIntervals;
        } else {
            int matchFirst = newInterval[0], matchSecond = newInterval[1], newLength = length + 1;
            boolean[] flag = new boolean[length];
            for (int i = 0; i < length; i++) {
                int curFirst = intervals[i][0], curSecond = intervals[i][1];
                if (((matchFirst >= curFirst && matchFirst <= curSecond) || (matchSecond >= curFirst && matchSecond <= curSecond)) ||
                        ((curFirst >= matchFirst && curFirst <= matchSecond) || (curSecond >= matchFirst && curSecond <= matchSecond))) {
                    // 有交集
                    matchFirst = Math.min(matchFirst, curFirst);
                    matchSecond = Math.max(matchSecond, curSecond);
                    flag[i] = true;
                    newLength--;
                }
            }
            int[][] newIntervals = new int[newLength][2];
            boolean added = false;
            int pos = 0;
            for (int i = 0; i < length; i++) {
                if (!flag[i]) {
                    if (added) {
                        newIntervals[pos++] = intervals[i];
                    } else {
                        if (matchSecond < intervals[i][0]) {
                            newIntervals[pos++] = new int[]{matchFirst, matchSecond};
                            added = true;
                        }
                        newIntervals[pos++] = intervals[i];
                    }
                }
            }
            if (!added) {
                newIntervals[pos++] = new int[]{matchFirst, matchSecond};
            }

            return newIntervals;
        }
    }

    public static void main(String[] args) {
        int[][] intervals = new int[][]{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}};
        int[] newInterval = new int[]{4, 8};
        for (int[] ints : insert(intervals, newInterval)) {
            for (int anInt : ints) {
                System.out.print(anInt + " ");
            }
            System.out.println();
        }
    }
}