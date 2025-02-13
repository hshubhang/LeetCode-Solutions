class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = best = curr = 0
        for right in range(len(prices)):
            while prices[left] > prices[right]:
                left += 1
            curr = prices[right] - prices[left]
            best = max(best, curr)
        
        return best