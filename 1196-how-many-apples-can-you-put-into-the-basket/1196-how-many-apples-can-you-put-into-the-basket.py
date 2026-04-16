class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        count = 0
        max_weight = 5000
        weight.sort()

        for i in range(len(weight)):

            if weight[i] <= max_weight:
                count += 1
                max_weight -= weight[i]
            
        
        return count

