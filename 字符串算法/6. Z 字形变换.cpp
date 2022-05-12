#include<iostream>
#include<string>
using namespace std;
class ConvertZStr {
public:
    string convert(string s, int rows) {
        if (rows <= 1) {
            return s;
        }
        string str;
        for (int i = 0; i < rows; i++) {
            int sum = 2 * (rows - 1);
            int gap = (rows - i - 1) * 2;
            for (int j = i; j < s.length(); ) {
                if (gap != 0) {
                    str += s[j];
                }
                j = j + gap;
                gap = sum - gap;
            }
        }
        return str;
    }
};
int main(){
    ConvertZStr convertZStr;
    string str = "ILOVECODINGEVERYDAY";
    cout<< convertZStr.convert(str,3)<<endl;
    cout<< convertZStr.convert(str,4)<<endl;
    return 0;
}