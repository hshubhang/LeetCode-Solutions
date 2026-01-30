class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        ans = []

        graph = {}

        for (a, b), i in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            graph[a][b] = i
         
            if b not in graph:
                graph[b] = {}
            graph[b][a] = 1/i

        def dfs(node, target, product, visited):
            if node == target:
                return product
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    result = dfs(neighbor, target, product * graph[node][neighbor], visited)
                    if result != -1:
                        return result

            return -1

        for i in range(len(queries)):
            
            visited = set()
            node, target = queries[i]
            if node not in graph or target not in graph:
                ans.append(-1)
                continue
            if node == target:
                ans.append(1.0)
                continue
            ans.append(dfs(node, target, 1.0, visited))

        return ans

