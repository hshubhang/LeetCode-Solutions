class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num_count = defaultdict(int)
        for i in nums:
            num_count[i] += 1
        
        return max((key for key in num_count if num_count[key] == 1), default= -1)
