#include <iostream>
#include <string>
#include <set>
using namespace std;

class Solution {
public:
    string getKSortStr(string str, int k) {
        set<string> MyHeap;
        for (int i = 1; i <= k; i++) {
            for (int j = 1; i + j <= str.size(); j++) {
                string temp_str;
                for (int k = j; k < i + j; k++)
                    temp_str.push_back(str[k - 1]);
                MyHeap.insert(temp_str);
            }
        }
        int count = 0;
        for (auto i = MyHeap.begin(); i != MyHeap.end(); i++) {
            count++;
            if (count == min((int) MyHeap.size(), k)) {
                return *i;
                break;
            }
        }
        return NULL;
    }
};

int main() {
    Solution solution;
    string s;
    int k;
    cin >> s;
    cin >> k;
    string results = solution.getKSortStr(s, k);
    cout << results;
}