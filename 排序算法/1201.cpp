#include <iostream>
using namespace std;
int f(int n)
{
    if (n <= 1) return n;

    return f(n - 2) + f(n - 1);
}
int main(){
    int t,n;
    cin >> t;
    while(t--){
        cin >> n;
        cout<<f(n)<<endl;
    }
    return 0;
}