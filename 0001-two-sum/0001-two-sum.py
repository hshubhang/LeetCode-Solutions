class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            second_number = target - nums[i]
            if second_number in hashmap and hashmap[second_number] != i:
                return [i, hashmap[second_number]]