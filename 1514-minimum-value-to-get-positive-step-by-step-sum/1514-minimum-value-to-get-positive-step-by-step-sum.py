class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]

        for i in range(1, len(nums)):
            prefix_sum[i] = nums[i] + prefix_sum[i - 1]

        smallest_sum = min(prefix_sum)
        if smallest_sum <= 0:

            ans = 1 - smallest_sum
        elif smallest_sum >= 0:
            ans = 1

        return ans
