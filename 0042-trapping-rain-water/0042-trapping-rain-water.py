class Solution:
    def trap(self, height: List[int]) -> int:
        point1 = 0
        point2 = len(height) - 1
        count = 0
        point1_max = 0
        point2_max = 0
        while point1 < point2:
            if height[point1] < height[point2]:
                point1_max = max(point1_max, height[point1])
                count += point1_max - height[point1]
                point1 += 1
            else:
                point2_max = max(point2_max, height[point2])
                count += point2_max - height[point2]
                point2 -= 1
        return count
