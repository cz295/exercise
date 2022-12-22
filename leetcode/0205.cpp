class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> mapping_s_to_t, mapping_t_to_s;
        bool find_t, find_s;
        for(auto i = 0; i < s.size(); ++i)
        {
            find_s = mapping_s_to_t.find(s[i]) != mapping_s_to_t.end();
            find_t = mapping_t_to_s.find(t[i]) != mapping_t_to_s.end();
            if (find_s || find_t)
            {
                if ((mapping_s_to_t[s[i]] != t[i]) || (mapping_t_to_s[t[i]] != s[i]))
                    return false;
            }
            else
            {
                mapping_s_to_t[s[i]] = t[i];
                mapping_t_to_s[t[i]] = s[i];
            }
        }
        return true; 
    }
};
