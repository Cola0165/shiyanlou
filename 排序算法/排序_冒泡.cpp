#include <iostream>
using namespace std;

void bubbleSort(int nums[],int size);
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
    bubbleSort(nums,size);
    return 0;
}

void bubbleSort(int nums[],int size) {
  // 每轮针对前面（size-i）个数进行排序
  for (int i = 0; i < size - 1; i++) {
    // cout<<"第" <<  (i + 1) << "轮交换开始" <<endl;
    // 每一轮排序，从第 0 个元素，到 size-1-i 个元素
    for (int j = 0; j < size - 1 - i; j++) {
      // 对比相邻的两个元素
      if (nums[j] < nums[j + 1]) {
        // 元素交换。使得大的元素在后面
        int temp = nums[j + 1];
        nums[j + 1] = nums[j];
        nums[j] = temp;
      }
      
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