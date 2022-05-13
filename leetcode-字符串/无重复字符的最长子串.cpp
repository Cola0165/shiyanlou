#include "iostream"

using namespace std;

#include "algorithm"
#include "vector"
#include "queue"
#include "set"
#include "map"
#include "string"
#include "stack"

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        int ans = 0;

        for (int i = 0; i < s.size(); i++)
            for (int j = i + 1; j <= s.size(); j++)
            {
                if (allUnique(s, i, j))
                    ans = max(ans, j - i);
            }
        return ans;
    }
    bool allUnique(string s, int begin, int end)
    {
        map<char, int> hash;
        for (int i = begin; i < end; i++)
        {
            if (hash.find(s[i]) != hash.end())
                return false;
            hash[s[i]] = i;
        }
        return true;
    }
};

int main() {

    string s;
    cin >> s;
    Solution *pSolution = new Solution;
    int i = pSolution->lengthOfLongestSubstring(s);
    cout << i << endl;
    return 0;
}