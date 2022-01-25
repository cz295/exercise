class Solution {
public:
    int search(vector<int>& nums, int target) {
        int i1 = 0, i2 = nums.size() - 1, mid_idx;
        if (i2 == -1)
            return -1;
        while(i1 < i2)
        {
            mid_idx = i1 + (i2 - i1) / 2;
            if(nums[mid_idx] == target)
            {
                return mid_idx;
            }
            else if (nums[mid_idx] > target)
            {
                i2 = mid_idx - 1;
            }
            else
            {
                i1 = mid_idx + 1;
            }
        }
        if(nums[i1] == target)
            return i1;
        else
            return -1;
    }
};
