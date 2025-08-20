class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []

        minheap = []
        heapq.heapify(minheap)

        available_tasks = []

        for idx, (enqueue_time, process_time) in enumerate(tasks):
            available_tasks.append((enqueue_time, process_time, idx))

        available_tasks.sort()
        n = len(tasks)
        time = 0
        i = 0

        while len(res) < n:
            if not minheap and i < n and time < available_tasks[i][0]:
                time = available_tasks[i][0]

            while i < n and available_tasks[i][0] <= time:
                eneque_time, processing_time, idx = available_tasks[i]
                heapq.heappush(minheap, (processing_time, idx))
                i += 1

            if minheap:
                processing_time, idx = heapq.heappop(minheap)
                res.append(idx)
                time += processing_time
            
        return res



