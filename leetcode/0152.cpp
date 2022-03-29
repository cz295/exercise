class Solution {
public:
    int maxProduct(vector<int>& nums) {
//         int smallest = 1, largest = 1, max_product = nums[0]; 
//         for(int i = 0; i < nums.size(); ++ i)
//         {

//             if(nums[i] > 0)
//             {
//                 smallest *= nums[i];
//                 if(largest > 0)
//                     largest *= nums[i];
//                 else
//                     largest = nums[i];
//                 max_product = max(max_product, largest);
//             }
//             else if (nums[i] < 0)
//             {
//                 int tmp = largest;
//                 if(smallest < 0)
//                     largest = smallest * nums[i];
//                 else
//                     largest = nums[i];
//                 if(tmp > 0)
//                     smallest = tmp * nums[i];
//                 else
//                     smallest = nums[i];
//                 max_product = max(max_product, largest);
//             }
//             else
//             {
//                 max_product = max(max_product, 0);
//                 smallest = largest = 1;
//             }
//         }
//         return max_product;
        
        int max_val = nums[0];
        int max_product = 1;
        int min_product = 1;
        for(int i = 0; i < nums.size(); ++ i)
        {
            if(nums[i] < 0)
            {
                swap(max_product, min_product);
            }
            max_product = max(max_product * nums[i], nums[i]);
            min_product = min(min_product * nums[i], nums[i]);
            max_val = max(max_val, max_product);
        }
        return max_val;
    }
};
