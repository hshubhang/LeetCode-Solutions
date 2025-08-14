class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            point1, point2 = i+1, len(nums) - 1
            while point1 < point2:
                target_sum = nums[i] + nums[point1] + nums[point2]
                if target_sum == 0:
                    results.append([nums[i], nums[point1],nums[point2]])
                    point1 += 1
                    point2 -= 1
                    while point1 < point2 and nums[point1] == nums[point1 - 1]:
                        point1 += 1
                    while point1 < point2 and nums[point2] == nums[point2 + 1]:
                        point2 -= 1
                elif target_sum < 0:
                    point1 += 1
                else:
                    point2 -= 1
        return results




