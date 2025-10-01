class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != (n-1):
            return False
        adjacency_list = {i : [] for i in range(n)}

        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)

        visited = set()

        def dfs(node):

            if node in visited:
                return
            
            visited.add(node)
            
            for neighbor in adjacency_list[node]:
                dfs(neighbor)
           
            if len(visited) == n:
                return True

            return False

        
        return dfs(0)
