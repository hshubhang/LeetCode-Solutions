class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ans = 0
        integerCount = Counter(arr)
        n = len(arr)
        half = ceil(n/2)
        removed = 0

        for number, count in integerCount.most_common():
            
            removed += count
            ans += 1
            if removed >= half:
                return ans

        return ans


            
        