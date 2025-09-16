class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mon_stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while mon_stack and temperatures[i] > temperatures[mon_stack[-1]]:

                indx = mon_stack.pop()
                ans[indx] = i - indx

            mon_stack.append(i)

        return ans
