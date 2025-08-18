class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        # A : 3 B:3
        maxHeap = [-cnt for cnt in count.values()]
        # -3 , -3
        heapq.heapify(maxHeap)
        time = 0
        queue = deque()

        while maxHeap or queue:
            time += 1 #time 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                # -3, -2
                if cnt:
                    queue.append((cnt, time + n))
                # -2 , 1 + 2 = 3
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time
