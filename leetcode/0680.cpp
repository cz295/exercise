class Solution {
public:
    bool isPalindrome(string &s, int i, int j)
    {
        int i1 = i, i2 = j;
        while (i1 < i2)
        {
            if(s[i1] == s[i2])
            {
                ++ i1;
                -- i2;
            }
            else
            {
                return false;
            }
        }
        return true;
    }
    
    bool validPalindrome(string s) {
        int i1 = 0, i2 = s.size() - 1;
        while(i1 < i2)
        {
            if(s[i1] == s[i2])
            {
                ++ i1;
                -- i2;
            }
            else
            {
                return isPalindrome(s, i1 + 1, i2) || isPalindrome(s, i1, i2 - 1);
            }
        }
        return true;
    }
};
