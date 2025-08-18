class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return s
        count = Counter(s)
        maxHeap = []
        
        if max(count.values()) > (len(s) + 1) // 2:
            return ""
        
        for char, cnt in count.items():    
            maxHeap.append((-cnt, char))
        heapq.heapify(maxHeap)

        res = []
        prev = [0, ""]

        while maxHeap or prev[0] < 0:
            if not maxHeap:
                return ""
            
            cnt, ch = heapq.heappop(maxHeap)
            res.append(ch)
            cnt += 1

            if prev[0] < 0:
                heapq.heappush(maxHeap, prev)

            prev = (cnt, ch)

        return "".join(res)

        
        