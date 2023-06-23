class Solution {
public:
    int maxSubArray(vector<int>& nums) {

        int currMax = nums[0], maxSum = nums[0];
        for(int i=1;i<nums.size();i++) {
            currMax = max(currMax + nums[i], nums[i]);
            maxSum = max(maxSum, currMax);
        }
        return maxSum;
        /*
        int running_sum = 0, max_sum = 0;
        for(int i = 0; i < nums.size(); ++ i)
        {
            if((nums[i] < 0) && (nums[i] + running_sum < 0))
            {
                running_sum = 0;
            }
            else
            {
                running_sum += nums[i];
                max_sum = max(max_sum, running_sum);
            }
        }
        if(max_sum == 0)
            return *max_element(nums.begin(), nums.end());
        else
            return max_sum;
        */
    }
};


