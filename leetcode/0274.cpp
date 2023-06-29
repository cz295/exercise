class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        std::sort(citations.begin(), citations.end(), std::greater<>());
        for(int i=0; i <n; ++i)
        {
            if(citations[i] < i + 1)
                return i;
        }
        return n;
    }
};
