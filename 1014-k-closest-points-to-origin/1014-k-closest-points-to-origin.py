class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_list = []
        heapq.heapify(points_list)
        res = []
        for x, y in points:

            distance = sqrt(x**2 + y**2)

            heapq.heappush(points_list, (distance, x, y))

        for i in range(k):
            closest_point = heapq.heappop(points_list)

            res.append([closest_point[1], closest_point[2]])

        return res

