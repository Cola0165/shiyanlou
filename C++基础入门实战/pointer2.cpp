#include<iostream>
using namespace std;

int main ()
{
    int i=3;
    int j=4;

    int &x=i; //定义引用 x，它是整型变量 i 的引用。
    int *s; //定义指针 s。
    s=&j; //指针 s 指向整型变量 j 的地址。

    cout << "初始化引用 x: " << x << endl;
    cout << "初始化指针 s: " << *s << endl;

    return 0;
}