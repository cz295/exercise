class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int>  res;
        int r_sum = 0;
        for(auto &val: nums)
        {
            r_sum += val;
            res.push_back(r_sum);
        }
        return res;
    }
};
