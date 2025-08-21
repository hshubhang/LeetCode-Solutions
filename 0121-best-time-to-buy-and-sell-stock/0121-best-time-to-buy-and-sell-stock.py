class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = best = curr = 0
        for right in range(len(prices)):
            while prices[left] > prices[right]:
                left += 1
            
            best = max(best, prices[right] - prices[left])

        return best
            