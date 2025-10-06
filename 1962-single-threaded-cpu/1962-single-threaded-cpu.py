class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        min_heap = []
        n = len(tasks)

        heapq.heapify(min_heap)
        task = sorted([(enqueue_time, process_time, i) for i, (enqueue_time, process_time) in enumerate(tasks)], key=lambda x:x[0])
        i = 0
        t = 1
        while i < n or min_heap:
            while i < n and task[i][0] <= t:
                et, pt, idx = task[i]
                heapq.heappush(min_heap, (pt, idx))
                i += 1
            if min_heap:
                process_time, index = heapq.heappop(min_heap)
                res.append(index)
                t += process_time
            else:
                t = max(t, task[i][0])

        return res



            

