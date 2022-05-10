#include <iostream>
using namespace std;
int f(int n)
{
    if (n <= 1) return n;

    return f(n - 2) + f(n - 1);
}
int main(){
    int n;
    cin >> n;
    cout<<f(n-1)<<endl;
    return 0;
}