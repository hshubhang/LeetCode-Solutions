class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()
        def backtrack(curr, i, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            #include element at index[i]
            curr.append(candidates[i])
            backtrack(curr, i+1, total + candidates[i])
            curr.pop()
            #skip element at index[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(curr, i+1, total)

        backtrack(curr, 0, 0)
        return res