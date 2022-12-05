class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sum_nums = 0;
        int left_sum = 0;
        for (auto &n: nums)
            sum_nums += n;
        for(int i = 0; i < nums.size(); ++i)        
        {
            if((sum_nums - left_sum - nums[i]) == left_sum)
                return i;
            left_sum += nums[i];
        }
        return -1;
    }
};
