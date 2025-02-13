class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        for i in nums:
            hashmap[i] += 1 
        for i in nums:
            if hashmap[i] == 1:
                return i  

        return -1 