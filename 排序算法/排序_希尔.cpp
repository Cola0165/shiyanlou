#include <iostream>
using namespace std;

void shellSort(int nums[],int size);
void printf(int nums[],int size);

int main() {
  int n;
    cin >> n;
    int nums[n];
    while(n--){
        cin >> nums[n];
    }
  // int nums[] = {98,90,34,56,21};
  int size =  sizeof(nums)/sizeof(nums[0]);
  // printf(nums,size);
  shellSort(nums,size);
  return 0;
}

void shellSort(int nums[],int size) {
  int times = 1;
  for (int gap = size / 2; gap > 0; gap /= 2) {
    // cout<<
      // "第" << (times++) << "轮希尔排序, gap= " << gap << " ,结果："
    // <<endl;
    for (int i = gap; i < size; i++) {
      int j = i;
      int temp = nums[j];
      while (j - gap >= 0 && temp > nums[j - gap]) {
        // 移动法
        nums[j] = nums[j - gap];
        j -= gap;
      }
      nums[j] = temp;
    }
  }
  printf(nums,size);
}

void printf(int nums[],int size){
  for (int i = size-1; i >= 0; i--) {
          cout<<nums[i]<<" ";
    }
    cout << endl;
    for (int i = 0; i < size; i++) {
        cout<<nums[i]<<" ";
    }
  // cout<<endl;
}