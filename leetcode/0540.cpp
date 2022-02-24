class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int i1 = 0, i2 = nums.size() - 1;
        if(nums.size() == 1)
            return nums[0];
        if(nums[0] != nums[1])
            return nums[0];
        if(nums[i2] != nums[i2 - 1])
            return nums[i2];
        
        int mid;
        while(i1 < i2)
        {
            mid = i1 + (i2 - i1) / 2;
            if ((nums[mid] != nums[mid + 1]) && (nums[mid] != nums[mid - 1]))
                return nums[mid];
            
            if(
                ((mid % 2 == 0) && nums[mid] == nums[mid + 1]) || 
                ((mid % 2 == 1) && nums[mid] == nums[mid - 1])
            )
                i1 = mid + 1;
            else
                i2 = mid - 1;
            //cout << i1 << " " << i2 << endl;
        }
        return nums[i1];
    }
};
