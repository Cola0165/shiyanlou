//给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。 
// 你可以假设数组中无重复元素。
// 示例 1:
// 输入: [1,3,5,6], 5
//输出: 2
// 示例 2:
// 输入: [1,3,5,6], 2
//输出: 1
// 示例 3:
// 输入: [1,3,5,6], 7
//输出: 4
// 示例 4:
// 输入: [1,3,5,6], 0
//输出: 0
// Related Topics 数组 二分查找
// 👍 676 👎 0
package com.zqh.leetcode.editor.cn;

//Java：搜索插入位置
public class P35SearchInsertPosition {
    public static void main(String[] args) {
        Solution solution = new P35SearchInsertPosition().new Solution();
//        System.out.println(solution.searchInsert(new int[]{1, 3}, 0));
        System.out.println(solution.searchInsert(new int[]{1, 3}, 2));
//        System.out.println(solution.searchInsert(new int[]{1, 3}, 4));
//        System.out.println(solution.searchInsert(new int[]{1, 3, 5, 6}, 0));
//        System.out.println(solution.searchInsert(new int[]{1, 3, 5, 6}, 5));
//        System.out.println(solution.searchInsert(new int[]{1, 3, 5, 6}, 2));
//        System.out.println(solution.searchInsert(new int[]{1, 3, 5, 6}, 7));
//        System.out.println(solution.searchInsert(new int[]{1, 2, 4, 6, 7}, 3));
//        System.out.println(solution.searchInsert(new int[]{3, 5, 7, 9, 10}, 8));
//        System.out.println(1 / 2);
        // TO TEST
    }

    //leetcode submit region begin(Prohibit modification and deletion)
    class Solution {
        public int searchInsert(int[] nums, int target) {
//            方案2：二分查找法
            return find(target, nums.length, nums);
//            方案1：循环判断
//            for (int i = 0; i < nums.length; i++) {
//                判断当前数是否大于目标值，大于说明在上一个索引
//                if (nums[i] > target) {
//                    return i == 0 ? 0 : i - 1;
//                }
//                如果是等于，就直接返回当前索引
//                if (nums[i] == target) {
//                    return i;
//                }
//                这里说面目标值大于所有数组值，就是最后的长度
//                if (i == nums.length - 1) {
//                    return nums.length;
//                }
//                这里说明是在中间  345那种
//                if (nums[i + 1] > target) {
//                    return i + 1;
//                }
//            }
//            return 0;
        }

        /**
         * 二分查找
         *
         * @param searchKey
         * @return
         */
        public int find(long searchKey, int maxArraySize, int[] array) {
            int lowerBound = 0;
            int upperBound = maxArraySize - 1;
            int curIndex;
            while (true) {
                //找出中间索引坐标
                curIndex = (lowerBound + upperBound) / 2;
                if (array[curIndex] == searchKey) {
                    //刚刚好相等就直接返回当前的坐标
                    return curIndex;
                }
                if (lowerBound > upperBound) {
                    //没有找到返回最大索引
                    if (curIndex == 0) {
                        //相同的时候,说明已经是处于最后的值了，但是被夹在中间,比如[1,3] 2
                        //第一次：index=(0+1)/2=0,array[0]=1<2,lowerBound=1
                        //第二次：index=(1+1)/2=1,array[1]=3>2,upperBound=0;
                        //第三次：index=(1+0)/2=0,1>0
                        return 1;
                    }
                    return curIndex + 1;
                }
                // 判断当前索引的值小于查找值的话
                if (array[curIndex] < searchKey) {
                    //太小了,开始的标记等于中间索引+1
                    lowerBound = curIndex + 1;
                } else {
                    //太大了
                    if (curIndex == 0) {
                        //相同的时候,说明已经是处于最后的值了，但是初始
                        return 0;
                    }
                    //结束的标记等于中间索引-1
                    upperBound = curIndex - 1;
                }
            }
        }
    }
    //leetcode submit region end(Prohibit modification and deletion)
}