#include "iostream"

using namespace std;

#include "algorithm"
#include "vector"
#include "queue"
#include "set"
#include "map"
#include "string"
#include "stack"

class Solution {
private:
    // 结果数组
    vector<int> result;
public:
    vector<int> searchRange(vector<int> &nums, int target) {
        // 升序排列的整数数组为空，则
        // 按照题目要求返回 [-1, -1]，
        // 注意这里不能返回空数组
        if (nums.empty()) {
            result.push_back(-1);
            result.push_back(-1);
            return result;
        }
        // 首先二分查找某个元素是否存在，如果不存在，则按照题目要求返回 [-1, -1]，
        bool b = binary_search(nums.begin(), nums.end(), target);
        if (!b) {
            result.push_back(-1);
            result.push_back(-1);
            return result;
        } else {
            // 由于搜索返回的是迭代器 iterator，所以这里需要减去数组指针，才能获取下标
            // 如果存在则先搜索以该元素开始的第一个元素
            auto iterator1 = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
            // 再搜索比该元素大的第一个元素
            auto iterator2 = upper_bound(nums.begin(), nums.end(), target) - nums.begin();

            result.push_back(iterator1);
            // iterator2是获取比该元素大的第一个元素， -1 就是最后一个 target 的索引
            result.push_back(iterator2 - 1);

            // 返回结果数组
            return result;
        }

    }
};

int main() {
    vector<int> nums = {5, 7, 7, 8, 8, 10};
    Solution *pSolution = new Solution;
    auto vector1 = pSolution->searchRange(nums, 8);
    if (!vector1.empty()) {
        cout << vector1[0] << " " << vector1[1] << endl;
    } else {
        cout << "空" << endl;
    }
    system("pause");
    return 0;
}

// class Solution
// {
// public:
//     vector<int> searchRange(vector<int> &nums, int target)
//     {
//         int start = -1, end = -1;
//         for (int i = 0; i < nums.size(); i++)
//         {
//             if (nums[i] == target)
//             {
//                 if (start == -1)
//                     start = i;
//                 end = i;
//             }
//         }
//         vector<int> ans;
//         ans.push_back(start);
//         ans.push_back(end);
//         return ans;
//     };
// };

// class Solution
// {
// public:
//     vector<int> searchRange(vector<int> &nums, int target)
//     {
//         int start = -1, end = -1;
//         for (int i = 0; i < nums.size(); i++)
//         {
//             if (nums[i] == target)
//             {
//                 if (start == -1)
//                     start = i;
//                 end = i;
//             }
//         }
//         vector<int> ans;
//         ans.push_back(start);
//         ans.push_back(end);
//         return ans;
//     };
// };

// class Solution
// {
// public:
//     vector<int> searchRange(vector<int> &nums, int target)
//     {
//         vector<int> res;
//         res.push_back(binary_search_begin(nums, target));
//         res.push_back(binary_search_end(nums, target));
//         return res;
//     }

// private:
//     int binary_search_begin(vector<int> nums, int target)
//     {
//         int lo = -1;
//         int hi = nums.size();
//         while (lo + 1 < hi)
//         {
//             int mid = lo + (hi - lo) / 2;
//             if (target > nums[mid])
//             {
//                 lo = mid;
//             }
//             else
//             {
//                 hi = mid;
//             }
//         }
//         if (hi == nums.size() || nums[hi] != target)
//         {
//             return -1;
//         }
//         else
//         {
//             return hi;
//         }
//     }
//     int binary_search_end(vector<int> nums, int target)
//     {
//         int lo = -1;
//         int hi = nums.size();
//         while (lo + 1 < hi)
//         {
//             int mid = lo + (hi - lo) / 2;
//             if (target < nums[mid])
//             {
//                 hi = mid;
//             }
//             else
//             {
//                 lo = mid;
//             }
//         }
//         if (lo == -1 || nums[lo] != target)
//         {
//             return -1;
//         }
//         else
//         {
//             return lo;
//         }
//     }
// };