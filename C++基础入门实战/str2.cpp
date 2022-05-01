#include <iostream>
using namespace std;

int main()
{
    string str1 = "Hello ";
    string str2 = "Shiyanlou!";

    str1.append(str2);//连接字符串。
    cout<<"连接 s1 和 s2："<<str1<<endl;

    cout<<"连接 s1 和 s2 后 str1 的长度："<<str1.length()<<endl; //计算字符串 str1 的长度。
    return 0;
}