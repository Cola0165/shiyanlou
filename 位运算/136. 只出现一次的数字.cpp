#include <iostream>
#include <vector>

using namespace std;

class SingleNumber {
public:
    int singleNumber(vector<int> nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
};

int main() {
    SingleNumber singleNumber;
    cout << singleNumber.singleNumber({4, 12, 34, 12, 4}) << endl;
    cout << singleNumber.singleNumber({4, 12, 34, 12, 4, 5, 34}) << endl;
}