class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        curr_profit, curr_enter = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] < curr_enter:
                curr_enter = prices[i]
            else:
                curr_profit = max(curr_profit, prices[i] - curr_enter)
        return curr_profit
