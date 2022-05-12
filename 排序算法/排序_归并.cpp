#include <iostream>
using namespace std;

// 声明函数
void mergeSort(int nums[],int size);
void printf(int nums[],int size);
void merge(int nums[], int left, int mid, int right);
void sort(int nums[], int left, int right,int size);

int main() {
    int n;
    cin >> n;
    int nums[n];
    while(n--){
        cin >> nums[n];
    }
    // int nums[] = {98, 90, 34, 56, 21, 11, 43, 61};
    int size =  sizeof(nums)/sizeof(nums[0]);
    mergeSort(nums,size);
    printf(nums,size);
    return 0;
}
// 排序入口
void mergeSort(int nums[],int size) {
    sort(nums, 0, size-1, size);
}
// 排序
void sort(int nums[], int left, int right,int size) {
    if (left >= right) {
      return;
    }
    int mid = left + ((right - left) / 2);
    // cout<<"left:" << left << " ,mid:" << mid << " ,right:" << right <<endl;
    // 排序左边
    sort(nums, left, mid,size);
    // 排序右边
    sort(nums, mid + 1, right,size);
    // 合并子数组
    merge(nums, left, mid, right);
    
  }

  void merge(int nums[], int left, int mid, int right) {
    int size = right-left+1;
    // 申请临时数组
    int tempNums[size];
    int i = 0;
    int index1 = left;
    int index2 = mid + 1;
    // 比较左右两部分的元素，哪个小，就把那个元素填入temp中
    while (index1 <= mid && index2 <= right) {
      // 左边的元素更小
      if (nums[index1] < nums[index2]) {
        tempNums[i] = nums[index1];
        i++;
        index1++;
      } else {
        // 右边的元素更小
        tempNums[i] = nums[index2];
        i++;
        index2++;
      }
    }
    // 如果左边还有元素剩下，则全部合并过去
    while (index1 <= mid) {
      tempNums[i] = nums[index1];
      i++;
      index1++;
    }
    // 如果右边有元素剩下，则把右边元素合并过去
    while (index2 <= right) {
      tempNums[i] = nums[index2];
      i++;
      index2++;
    }
    // 把最后的排序结果复制到原数组中
    for (i = 0; i < size; i++) {
      nums[left + i] = tempNums[i];
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