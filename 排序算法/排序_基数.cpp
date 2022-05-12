#include <iostream>
#include <cstring>
using namespace std;

// 声明函数
void radixSort(int nums[],int size);
void printf(int nums[],int size);


int main() {
    int n;
    cin >> n;
    int nums[n];
    while(n--){
        cin >> nums[n];
    }
    // int nums[] = {98, 90, 34, 56, 21, 11, 43, 61};
    int size =  sizeof(nums)/sizeof(nums[0]);
    radixSort(nums,size);
    return 0;
}

void radixSort(int nums[],int size) {
  int max = nums[0];
  // 指数，从个位到十位到百位...
  int exp;
  // 遍历得到最大值
    for (int i=0;i<size;i++) {
    if (nums[i] > max) {
      max = nums[i];
    }
  }
  // 从个位开始，对数组每一位进行排序
  for (exp = 1; max / exp > 0; exp = exp * 10) {
    // 临时数组
    int tempNums[size];
    // 数值 0-9，桶的个数固定为 10
      int buckets[10] = {0,0,0,0,0,0,0,0,0,0};
    // buckets 中存储的其实是数据出现的次数
    for (int i=0; i<size; i++) {
      buckets[(nums[i] / exp) % 10]++;
    }
    // 每一个值等于前面的元素次数加上自身（类似计数排序）
    for (int i = 1; i < 10; i++) {
      buckets[i] += buckets[i - 1];
    }
    // 从后往前遍历，将元素写会临时数组
    for (int i = size - 1; i >= 0; i--) {
      tempNums[buckets[(nums[i] / exp) % 10] - 1] = nums[i];
      buckets[(nums[i] / exp) % 10]--;
    }
    // 将有序元素 tempNums 赋给 nums
    memcpy(nums,tempNums,size*sizeof(int));
    
  }
  printf(nums,size);
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