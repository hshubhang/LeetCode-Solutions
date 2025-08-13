class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left < right:
            mid = floor(left + (right - left) / 2)

            division = [math.ceil(x / mid) for x in nums]
            total = sum(division)
            if total > threshold:
                left = mid + 1
            else:
                right = mid

        return left
