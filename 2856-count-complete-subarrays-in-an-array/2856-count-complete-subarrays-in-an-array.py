class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_count = len(set(nums))
        window_map = defaultdict(int)
        left = 0
        right = 0
        count = 0
        for left in range(len(nums)):
            while right < len(nums) and len(window_map) < unique_count:
                window_map[nums[right]] += 1
                right += 1
            if len(window_map) == unique_count:
                count += (len(nums) - right + 1)

            window_map[nums[left]] -= 1
            if window_map[nums[left]] == 0:
                del window_map[nums[left]]
            
        return count

