class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0

        for element in range(len(nums)):
            if nums[element] % 3 == 0:
                continue

            if nums[element] % 3 == 1:
                nums[element] -= 1
                count +=1
            
            if nums[element] % 3 == 2:
                nums[element] += 1
                count += 1

        return count