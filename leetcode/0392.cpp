class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i_s = 0, i_t = 0;

        if (s.size() == 0)
            return true;
        if (t.size() == 0)
            return false; 

        while((i_s < s.size()) && (i_t < t.size()))
        {
            if(s[i_s] == t[i_t])
            {
                ++ i_s;
            }
            ++ i_t; 
        }
        return i_s == s.size();
    }
};
