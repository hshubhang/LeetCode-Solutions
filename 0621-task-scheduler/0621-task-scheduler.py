class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for character in tasks:
            freq[ord(character) - ord('A')] += 1

        
        pq = [-frequency for frequency in freq if frequency > 0]
        heapq.heapify(pq)

        time = 0

        while pq:
            cycle = n+1
            store = []
            taskCount = 0
            while cycle > 0 and pq:
                top = -heapq.heappop(pq)
                if top > 1:
                    top -= 1
                    store.append(-top)
                cycle -= 1
                taskCount += 1
            for x in store:
                heapq.heappush(pq, x)

            time += taskCount if not pq else n+1

        return time  
