#include <iostream>
#include <sstream>
#include <vector>
#include <set>
using namespace std;

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        int sLen = strs.size();

        if (sLen == 0)
            return "";

        string dst = "";
        int minLen = 100;
        int minIndex = 0;

        for (int i = 0; i < sLen; ++i)
        {
            int len = strs[i].length();
            if (len < minLen)
            {
                minLen = len;
                minIndex = i;
            }
        }

        for (int i = 0; i < strs[minIndex].length(); ++i)
        {
            set<char> ch;

            for (auto iter : strs)
                ch.insert((iter)[i]);

            int setLens = ch.size();

            if (setLens > 1)
                break;
            if (setLens == 1)
                dst += *ch.begin();
        }

        return dst;
    }
};

int main() {
    Solution solution;
    string inputStr;
    cin >> inputStr;
    stringstream ss(inputStr);
    string str;
    vector<string> strs;
    while (getline(ss, str, ','))
	{
        strs.push_back(str);
	}
    cout << solution.longestCommonPrefix(strs) << endl;
}