class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        target = len(nums) - 1
        for i, jump in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + jump)
            if farthest >= target:
                return True


            
