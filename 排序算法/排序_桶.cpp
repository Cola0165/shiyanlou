#include <iostream>
#include <climits>
#include <algorithm>
#include "vector"
using namespace std;

// 声明函数
void bucketSort(int nums[],int size);
void printf(int nums[],int size);

int main() {
    int n;
    cin >> n;
    int nums[n];
    while(n--){
        cin >> nums[n];
    }
    // int nums[] = {11, 9, 11, 13, 19, 14, 16, 14, 8, 17};
    int size =  sizeof(nums)/sizeof(nums[0]);
    bucketSort(nums,size);
    printf(nums,size);
    return 0;
}

void bucketSort(int nums[] ,int size) {
  // 遍历数组获取最大最小值
  int max = INT_MIN;
  int min = INT_MAX;
  for (int i = 0; i < size; i++) {
    max = std::max(max, nums[i]);
    min = std::min(min, nums[i]);
  }

  // 计算桶的数量
  int bucketNum = (max - min) / size + 1;
  // cout << "最小：" << min << "，最大：" << max << ",桶的数量：" << bucketNum << endl;
  std::vector<std::vector<int>> buckets(bucketNum);
  // 将每个元素放入桶
  for (int i = 0; i < size; i++) {
    int num = (nums[i] - min) / size;
    buckets[num].push_back(nums[i]);
  }

  // 对每个桶内部进行排序
  for (int i = 0; i < buckets.size(); i++) {
      if (buckets[i].empty()) continue;
      std::sort(buckets[i].begin(), buckets[i].end());
  }

  // 将桶的元素复制到数组中
  int index = 0;
  for (int i = 0; i < buckets.size(); i++) {
    for (int j = 0; j < buckets[i].size(); j++) {
      nums[index++] = buckets[i][j];
    }
  }
}

void printf(int nums[],int size){
    for (int i = 0; i < size; i++) {
        cout<<nums[i]<<" ";
    }
    cout << endl;
    for (int i = size-1; i >= 0; i--) {
          cout<<nums[i]<<" ";
    }
    // cout<<endl;
}