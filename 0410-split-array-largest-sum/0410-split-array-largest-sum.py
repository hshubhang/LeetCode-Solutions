class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        low = max(nums)
        high = sum(nums)
        result = -1
        while low <= high:

            mid = (low + high) // 2  #10 + 32 /2 = 42 / 2 = 21
            
            countSplits = self.max_split(nums, mid)

            if countSplits <= k:
                high = mid - 1
                result = mid
            else:
                low = mid + 1

        return result
    
    def max_split(self, nums, split):

        no_of_splits = 1 
        max_split = 0

        for i in range(len(nums)):

            if max_split + nums[i] <= split:
                max_split += nums[i]

            else:
                no_of_splits += 1
                max_split = nums[i]

        return no_of_splits

    

