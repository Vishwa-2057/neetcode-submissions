class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_prft = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                cur_prft = prices[r] - prices[l]
                max_prft =  max(cur_prft, max_prft)
            elif prices[r] < prices[l]:
                l = r
            r+=1
        
        return max_prft


        