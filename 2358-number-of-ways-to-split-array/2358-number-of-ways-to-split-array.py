class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        for k in range(len(nums)- 1):
            if prefix[k] >= prefix[-1] - prefix[k]:
                count += 1
        
        return count
        