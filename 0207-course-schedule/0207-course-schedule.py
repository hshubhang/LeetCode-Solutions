class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)


        state = [0] * numCourses

        def dfs(node):

            if state[node] == 1:
                return False
            if state[node] == 2:
                return True

            state[node] = 1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

        
            state[node] = 2
            return True

        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False

        return True

        



