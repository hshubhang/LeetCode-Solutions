class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(len(nums) - 2, -1 , -1):
            suffix[j] = suffix[j+1] * nums[j+1]
            prefix[j] = prefix[j] * suffix[j]

        return prefix

            
