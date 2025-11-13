class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = best = curr = 0

        for right in range(len(prices)):

            while left != right and  prices[right] < prices[left]:
                left += 1
            curr = prices[right] - prices[left]
            best = max(best, curr)

        return best
