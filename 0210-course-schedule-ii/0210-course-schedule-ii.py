class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = {i : [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            adjacency_list[course].append(prerequisite)

        state = [0] * numCourses
        ans = []
        def dfs(node):

            if state[node] == 1:
                return False
            
            if state[node] == 2:
                return True


            state[node] = 1

            for neighbor in adjacency_list[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2
            ans.append(node)
            return True
            
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []
            
        return ans

