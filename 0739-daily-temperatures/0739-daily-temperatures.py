class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                previous_index = stack.pop()
                answer[previous_index] = i - previous_index
            stack.append(i)
        return answer