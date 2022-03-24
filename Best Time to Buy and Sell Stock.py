# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, left, right = 0, 0, 1

        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[right] > prices[left]:
                maxProfit = max(currentProfit, maxProfit)
            else:
                left = right
            right += 1
        return maxProfit


