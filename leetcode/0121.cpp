class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0], max_profit = 0;
        for(int i = 1; i < prices.size(); ++i)
        {
            if(prices[i] < buy)
                buy = prices[i];
            else
                max_profit = max(max_profit, prices[i] - buy);
        }
        return max_profit;
    }
};
