class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_step = 0;
        for(auto i = 0; i < nums.size(); ++i)
        {
            if(max_step > nums.size() - 1)
                return true;
            if(max_step < i)
                return false;
            max_step = max(max_step, nums[i] + i);
        }
        return true;
    }
};
