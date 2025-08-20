class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        res = []
        minheap = []
        heapq.heapify(minheap)
        
        available_tasks = []

        for idx, (eneque_time, processing_time) in enumerate(tasks):
            available_tasks.append((eneque_time, processing_time, idx))
        available_tasks.sort()
        
        number_of_tasks = len(tasks)
        time = 0
        i = 0
        while len(res) < number_of_tasks:

            if not minheap and i < number_of_tasks and time < available_tasks[i][0]:
                time = available_tasks[i][0]

            while i < number_of_tasks and available_tasks[i][0] <= time:
                et, pt, idx = available_tasks[i]
                heapq.heappush(minheap, (pt, idx))
                i+=1

            if minheap:
                pt, idx = heapq.heappop(minheap)
                res.append(idx)
                time += pt
        
        return res
            


