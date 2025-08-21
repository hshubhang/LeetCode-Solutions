class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = best = sum(nums[:k])
        
        for right in range(k, len(nums)):
            curr += nums[right] - nums[right - k]
            best = max(best, curr)

        return best/k