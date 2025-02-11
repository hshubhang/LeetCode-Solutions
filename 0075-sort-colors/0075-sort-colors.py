class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for head in range(len(nums)):
            for head1 in range(head+1, len(nums)):
                if nums[head] > nums[head1]:
                    nums[head], nums[head1] = nums[head1], nums[head]
                

