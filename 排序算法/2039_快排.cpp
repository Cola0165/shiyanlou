#include <iostream>
using namespace std;

void quickSort(int nums[],int size);
void quickSort(int nums[], int left, int right,int size);
void printf(int nums[],int size);

int main() {
    int n;
    cin >> n;
    int nums[n];
    while(n--){
        cin >> nums[n];
    }
    // int nums[] = {61, 90, 34, 56, 21, 11, 43, 68};
    int size =  sizeof(nums)/sizeof(nums[0]);
    // printf(nums,size);
    quickSort(nums,size);
    printf(nums,size);
    return 0;
}

void quickSort(int nums[],int size) {
    quickSort(nums, 0, size - 1,size);
  }

void quickSort(int nums[], int left, int right,int size) {
    // cout<<"[" << left << " , " << right << "]"<< endl;
    if (left < right) {
      // 区间左边界是 i，右边界是 j，基准值是 standardNum
      int i = left, j = right, standardNum = nums[left];
      while (i < j) {
        // 从右向左找第一个小于 standardNum的数
        while (i < j && nums[j] >= standardNum) {
          j--;
        }
        // cout<<
          // "standardNum:" <<
          // standardNum <<
          // ", 第1个小于等于standardNum的数： " <<
          nums[j];
        if (i < j) {
          // nums[i]已经被保存到standardNum，将nums[j]写到左边
          nums[i] = nums[j];
          i++;
        }
        // 从左向右找第一个大于等于 standardNum 的数
        while (i < j && nums[i] < standardNum) {
          i++;
        }
        // cout<<", 第1个大于等于standardNum的数： " << nums[i]<<endl;
        if (i < j) {
          // 将较大的数写到右边
          nums[j] = nums[i];
          j--;
        }
      }
      // 将基准值写到中间
      nums[i] = standardNum;
      // printf(nums,size);
      quickSort(nums, left, i - 1, size);
      
      quickSort(nums, i + 1, right, size);
    }
  }

void printf(int nums[],int size){
    for (int i = size-1; i >= 0; i--) {
        cout<<nums[i]<<endl;
    }
    // cout<<endl;
}