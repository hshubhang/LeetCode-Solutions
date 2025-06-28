class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [nums[0]]
        ans = []

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i - 1])

        for i in queries:
            
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if prefix[mid] > i:
                    right = mid - 1
                else:
                    left = mid + 1

            ans.append(left)

        return ans
            


            