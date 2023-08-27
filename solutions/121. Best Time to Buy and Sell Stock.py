class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_pointer = 0
        max_profit = 0
        for r_pointer in range(len(prices)):     
            if prices[r_pointer] < prices[l_pointer]:
                l_pointer = r_pointer
            else:
                max_profit =  max(max_profit, prices[r_pointer] - prices[l_pointer])
        return max_profit
