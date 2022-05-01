#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    char str1[18] = "Hello ";
    char str2[11] = "Shiyanlou!";

    strcat(str1,str2);//连接字符串。
    cout<<"连接 str1 和 str2："<<str1<<endl;

    cout<<"连接 str1 和 str2 后 str1 的长度："<<strlen(str1)<<endl; //计算字符串 str1 的长度。
    return 0;
}