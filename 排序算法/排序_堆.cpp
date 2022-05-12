#include <iostream>
using namespace std;

// 声明函数
void heapSort(int nums[],int size);
void printf(int nums[],int size);
void adjustHeap(int nums[], int i, int length);
void swap(int nums[], int a, int b);

int main() {
    int n;
    cin >> n;
    int nums[n];
    while(n--){
        cin >> nums[n];
    }
    // int nums[] = {98, 90, 34, 56, 21, 11, 43, 61};
    int size =  sizeof(nums)/sizeof(nums[0]);
    heapSort(nums,size);

    return 0;
}

void heapSort(int nums[],int size) {
  // 首先需要构建最大堆
  for (int i = size / 2 - 1; i >= 0; i--) {
    // 从第一个非叶子结点调整结构，大的往上走
    adjustHeap(nums, i, size);
  }
  // printf(nums,size);
  // cout<< "-----------------------------" << endl;
  // 交换元素和调整
  for (int j = size - 1; j > 0; j--) {
    // 将堆顶元素与末尾元素交换
    swap(nums, 0, j);
    // 重新调整，大的元素往上交换
    adjustHeap(nums, 0, j);
    // cout<< "-----------------------------" << endl;
  }
  printf(nums,size);
}

/**
 * 调整大顶堆
 */
void adjustHeap(int nums[], int i, int length) {
  // 取出当前元素
  int temp = nums[i];
  //从左节点开始
  for (int k = i * 2 + 1; k < length; k = k * 2 + 1) {
    // 如果右节点更大，那么指向右节点
    if (k + 1 < length && nums[k] < nums[k + 1]) {
      k++;
    }
    // 子节点的值直接给父节点
    if (nums[k] > temp) {
      nums[i] = nums[k];
      i = k;
    } else {
      break;
    }
    // printf(nums,length);
  }
  // 最后将最上面的节点置，放到当前的节点
  nums[i] = temp;
}

/**
 * 交换元素
 */
void swap(int nums[], int a, int b) {
  int temp = nums[a];
  nums[a] = nums[b];
  nums[b] = temp;
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