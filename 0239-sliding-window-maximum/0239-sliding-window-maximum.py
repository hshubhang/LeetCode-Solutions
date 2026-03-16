class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        minheap = []
        heapq.heapify(minheap)


        for i in range(len(nums)):
            heapq.heappush(minheap, (- nums[i], i))

        
            while minheap[0][1] < i - k + 1:
                heapq.heappop(minheap)

            
            if i >= k - 1:
                ans.append(-minheap[0][0])

        return ans



        