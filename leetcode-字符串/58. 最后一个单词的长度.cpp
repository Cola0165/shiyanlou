#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int lengthOfLastWord(string s) {
        int n=s.size();
        int i=n-1;
        while(s[i]==' ')
        {
            i--;
        }
        int j=i;
        while(j!=0&&s[j-1]!=' ')
        {
            j--;
        }
        return i-j+1;
    }
};

int main(){
    Solution solution;
    string s;
    getline(cin,s);
    cout << solution.lengthOfLastWord(s) << endl;
    return 0;
}

// #include <sstream>
// class Solution
// {
// public:
//     int lengthOfLastWord(string s)
//     {
//         string word;
//         stringstream ss(s);
//         while (ss >> word)
//         {
//         }
//         return word.size();
//     }
// };

// class Solution
// {
// public:
//     int lengthOfLastWord(string s)
//     {
//         int countWord = 0;
//         for (int index = 0; index < s.size(); index++)
//         {
//             if (s[index] == ' ')
//             {
//                 if (index != s.size() - 1 && s[index + 1] != ' ')
//                 {
//                     countWord = 0;
//                     continue;
//                 }
//                 else
//                     continue;
//             }
//             countWord++;
//         }
//         return countWord;
//     }
// };

// #include <vector>
// class Solution
// {
// public:
//     int lengthOfLastWord(string s)
//     {
//         if (s.empty())
//             return 0;
//         vector<string> word;
//         int begin, lenWord = 0;
//         for (int i = 0; i < s.size(); i++)
//         {
//             if ((i == 0 && s[i] != ' ') || (i != 0 && s[i - 1] == ' ' && s[i] != ' '))
//             {
//                 begin = i;
//                 lenWord++;
//                 if (i == s.size() - 1)
//                 {
//                     word.push_back(s.substr(begin, lenWord));
//                     break;
//                 }
//             }
//             else if (s[i] != ' ' && i != s.size() - 1)
//             {
//                 lenWord++;
//             }
//             else if (i != 0 && s[i - 1] != ' ' && s[i] == ' ')
//             {
//                 word.push_back(s.substr(begin, lenWord));
//                 lenWord = 0;
//             }
//             else if (s[i] != ' ' && i == s.size() - 1)
//             {
//                 word.push_back(s.substr(begin, lenWord + 1));
//             }
//         }
//         if (word.empty())
//             return 0;
//         else
//             return word[word.size() - 1].size();
//     }
// };