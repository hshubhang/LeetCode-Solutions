class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(curr, i, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            backtrack(curr, i, total + candidates[i])
            curr.pop()
            backtrack(curr, i+1, total)

        backtrack(curr, 0, 0)
        return res


            
        