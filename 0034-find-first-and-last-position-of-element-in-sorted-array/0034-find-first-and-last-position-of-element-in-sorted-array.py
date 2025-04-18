class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        def findLeft():
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left if nums[left] == target else -1
            
        def findRight():
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left + 1) // 2 
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            return right if nums[right] == target else -1

        leftIndex = findLeft()
        if leftIndex == -1:
            return [-1, -1]  
        rightIndex = findRight()

        return [leftIndex, rightIndex]