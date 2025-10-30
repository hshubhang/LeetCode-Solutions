class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        length = 0
        hashmap = {}
        hashmap[0] = -1
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1

            if count in hashmap:
                length = max(length, i - hashmap[count])
            else:
                hashmap[count] = i

        return length





            