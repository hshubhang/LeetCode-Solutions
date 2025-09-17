class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        restricted_set = set(restricted)
        if 0 in restricted_set:
            return 0
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor in restricted_set:
                    continue
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

            
        seen = {0}
        
        dfs(0)

        return len(seen)