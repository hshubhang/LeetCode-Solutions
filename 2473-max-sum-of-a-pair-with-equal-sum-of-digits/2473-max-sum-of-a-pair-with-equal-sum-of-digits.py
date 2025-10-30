class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        digit_sums = [sum(int(d) for d in str(num)) for num in nums]
        maximum_addition = -1
        hashmap = defaultdict(list)

        for i in range(len(nums)):
            hashmap[digit_sums[i]].append(nums[i])

        for value in hashmap.values():
            if len(value) > 1:
                value.sort(reverse=True)
                addition = value[0] + value[1]
                maximum_addition = max(maximum_addition, addition)
            

        
        return maximum_addition