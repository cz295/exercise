class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        for(auto i = 0; i < prices.size() - 1; ++i)
        {
            int pc_diff = prices[i + 1] - prices[i];
            if(pc_diff > 0)
                max_profit += pc_diff;
        }
        return max_profit; 
    }
};
