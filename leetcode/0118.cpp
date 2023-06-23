class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> x; 
        x.push_back(vector<int> {1});
        for(int i = 1; i < numRows; ++i)
        {
            vector<int> tmp(i + 1, 0); 
            tmp[0] = tmp[i] = 1;
            for(int j = 1; j < i; ++j)
            {
                tmp[j] = x[i - 1][j - 1] + x[i - 1][j];
            }
            x.push_back(tmp);
        }
        return x;
    }
};
