#include <iostream>
using namespace std;

void selectionSort(int nums[],int size);
void printf(int nums[],int size);

int main() {
    int n;
    cin >> n;
    int nums[n];
    while(n--){
        cin >> nums[n];
    }
  //  int nums[] = {98,90,34,56,21};
   int size =  sizeof(nums)/sizeof(nums[0]);
  //  printf(nums,size);
   selectionSort(nums,size);
   return 0;
}

void selectionSort(int nums[],int size) {
  int times = 0;
  int minIndex;
  for (int i = 0; i < size - 1; i++) {
    // cout<< "第" << (i + 1) << "轮选择开始："<<endl;
    minIndex = i;
    for (int j = i + 1; j < size; j++) {
      times++;
      if (nums[j] > nums[minIndex]) {
        minIndex = j;
      }
    }
    // cout<<"交换 " << nums[i] << "和" << nums[minIndex]<<endl;
    int temp = nums[i];
    nums[i] = nums[minIndex];
    nums[minIndex] = temp;
    
  }
  //  cout<<"比较次数："<< times<<endl;
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
  //  cout<<endl;
}