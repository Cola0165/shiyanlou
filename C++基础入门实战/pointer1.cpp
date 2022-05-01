#include<iostream>
using namespace std;

int main ()
{
    int po1=6; //定义 int 型变量 po1，赋值为 6。
    int *p=&po1; //指针变量 p 指向变量 po1 的地址。

    cout << "获取指针所指变量的值: "<<*p<<endl;
    cout << "获取指针的内存地址: "<<&p<<endl;
    return 0;
}