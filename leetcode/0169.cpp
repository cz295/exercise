class Solution {
public:
    int majorityElement(vector<int>& nums) {
        map<int, int> nums_count;
        int max_count = 0, max_val = -1;
        for(auto val: nums)
        {
            if(nums_count.find(val) == nums_count.end())
            {
                nums_count[val] = 1;
            }
            else
            {
                nums_count[val] += 1;
            }
            if(nums_count[val] > max_count)
            {
                max_count = nums_count[val];
                max_val = val;
            }
        }
        return max_val; 
    }
};
