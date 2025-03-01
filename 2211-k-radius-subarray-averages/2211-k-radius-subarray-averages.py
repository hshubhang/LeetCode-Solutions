class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2 * k + 1:
            return ([-1] * len(nums))
        elif k == 0:
            return nums
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i+1] = (nums[i] + prefix[i])
        radius_arr = [-1] * len(nums)
        for i in range(k, len(nums) - k):
            left = i - k
            right = i + k
            total_sum = prefix[right + 1] - prefix[left]
            radius_arr[i] = total_sum // (2 * k + 1)
        return radius_arr


        
