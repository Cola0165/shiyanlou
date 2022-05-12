#include <iostream>
using namespace std;

void insertionSort(int nums[],int size);
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
    insertionSort(nums,size);
    return 0;
}

void insertionSort(int nums[],int size) {
    if (nums == NULL) {
      return;
    }
    int index, temp;
    for (int i = 1; i < size; i++) {
      // 当前选择插入的元素前面一个索引值
      index = i - 1;
      // 当前需要插入的元素
      temp = nums[i];
      while (index >= 0 && nums[index] < temp) {
        nums[index + 1] = nums[index];
        index--;
      }
      // 插入空出来的位置
      nums[index + 1] = temp;
      // cout<<"第" << i << "轮插入结果："<<endl;
      
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