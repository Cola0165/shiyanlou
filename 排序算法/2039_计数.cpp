#include <iostream>
using namespace std;

// 声明函数
void countSort(int nums[],int size);
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
    countSort(nums,size);
    return 0;
}

void countSort(int nums[],int size) {
  int max = nums[0];
  int min = nums[0];
  for (int i = 1; i < size; i++) {
    if (nums[i] > max) {
      max = nums[i];
    }
    if (nums[i] < min) {
      min = nums[i];
    }
  }
  // cout<< "min:" << min << ",max:" << max << endl;
  int count = max - min;
  int *countNums = new int[count + 1];

  // 初始化计数为0（C++与Java最大的不同之处之一）
  for (int i = 0; i < count + 1; i++) {
      countNums[i] = 0;
  }
  // 计数
  for (int i = 0; i < size; i++) {
    countNums[nums[i] - min]++;
  }
  // cout<< "countNums: ";
  // printf(countNums,count+1);
  int sum = 0;
  // 后面的元素等于前面元素加上自身
  for (int i = 0; i < count + 1; i++) {
    sum += countNums[i];
    countNums[i] = sum;
  }
  // cout<< "countNums: ";
  // printf(countNums,size);
  int *newNums = new int[size];
  for (int i = size - 1; i >= 0; i--) {
    /**
     * nums[i] - min 表示原数组 nums 里面第i位置对应的数在统计数组里面的位置索引
     */
    newNums[countNums[nums[i] - min] - 1] = nums[i];
    countNums[nums[i] - min]--;
  }
  printf(newNums,size);
}

void printf(int nums[],int size){
    for (int i = size-1; i >= 0; i--) {
        cout<<nums[i]<<endl;
    }
    // cout<<endl;
}