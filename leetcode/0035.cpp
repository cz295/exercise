class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int i1 = 0, i2 = nums.size() - 1, mid;
        while(i1 < i2)
        {
            mid = i1 + (i2 - i1) / 2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] > target)
                i2 = mid - 1;
            else
                i1 = mid + 1;
        }
        if(nums[i1] == target)
            return i1;
        else if (nums[i1] > target)
            return i1;
        else
            return i1 + 1;
        
    }
};
