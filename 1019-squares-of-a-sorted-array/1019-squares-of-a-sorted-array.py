class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        first = 0
        last = len(nums) -1
        for i in range(n-1, -1,-1):
            if abs(nums[first]) < abs(nums[last]):
                square = nums[last]
                last -= 1
            else:
                square = nums[first]
                first += 1
            
            result[i] = square * square
         
        return result