class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_list = []
        for x, y in points:
            distance = sqrt(x**2 + y**2)
            points_list.append((distance, (x, y)))
        heapq.heapify(points_list)
        ans = []
        for _ in range(k):
            _, coord = heapq.heappop(points_list)
            ans.append([coord[0], coord[1]])

        return ans