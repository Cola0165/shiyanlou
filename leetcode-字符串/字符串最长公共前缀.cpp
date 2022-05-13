#include <iostream>
#include <sstream>
#include <vector>
#include <set>
using namespace std;

class Solution
{
public:
    int longestCommonPrefix(vector<string> &strs)
    {
        int sLen = strs.size();

        if (sLen == 0)
            return 0;

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

        return dst.size();
    }
};

int main() {
    Solution solution;
    int n,x,y;
    string inputStr;
    cin >> n;
    vector<string> strss;
    while (n--)
	{
        cin >> inputStr;
        strss.push_back(inputStr);
	}
    while(cin >> x >> y)
    {
        vector<string> strs;
        strs.push_back(strss[x-1]);
        strs.push_back(strss[y-1]);
        cout << solution.longestCommonPrefix(strs) << endl;
    }
}