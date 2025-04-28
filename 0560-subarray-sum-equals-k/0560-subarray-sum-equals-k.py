class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        curr_sum = 0
        hashmap = {0: 1}
        for i in range(len(nums)):
            curr_sum += nums[i]
        
            if curr_sum-k in hashmap:
                count += hashmap[curr_sum - k]

            hashmap[curr_sum] = hashmap.get(curr_sum, 0) + 1

        return count


