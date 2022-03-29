class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int n = nums.size();
        if(n <= 2)
            return true;
        else
        {
            int cnt = 0, curr_high = 0;
            for(int i = 1; i < n; ++ i)
            {
                if(nums[i] < nums[i - 1])
                {
                    if(i == n - 1)
                        cnt += 1;
                    else
                    {
                        if(nums[i + 1] < nums[i - 1])
                        {
                            if(nums[i + 1] < nums[i])
                                return false;
                            else
                            {
                                if(nums[i + 1] >= curr_high && nums[i] >= curr_high)
                                {
                                    cnt += 1;
                                    curr_high = nums[i];
                                }
                                else
                                    return false;
                            }
                        }
                        else
                        {
                            cnt += 1;
                            curr_high = nums[i - 1];
                        }
                    }
                }
                else
                {
                    curr_high = nums[i - 1];
                }
                if(cnt >= 2)
                    return false;
            }
        }
        return true;

    }
};
