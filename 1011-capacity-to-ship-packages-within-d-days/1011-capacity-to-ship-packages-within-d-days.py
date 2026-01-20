class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)

        if len(weights) < days:
            return -1

        result = -1

        while low <= high:

            mid = low + (high - low) // 2

            count_days = self.max_weight(weights, mid)

            if count_days <= days:
                high = mid - 1
                result = mid
            else:
                low = mid + 1
        
        return result



    def max_weight(self, weights: List[int], ship_capacity: int) -> int:

        day = 1
        max_capacity = 0

        for i in range(len(weights)):

            if max_capacity + weights[i] <= ship_capacity:
                max_capacity += weights[i]

            else:
                day += 1
                max_capacity = weights[i]

        return day

    