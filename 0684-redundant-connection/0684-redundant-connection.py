class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque

        adjacency_list = defaultdict(list)
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        # edge -> input index (normalize undirected edges)
        input_index = {}
        for i, (u, v) in enumerate(edges):
            input_index[(min(u, v), max(u, v))] = i

        parent = {}          # child -> parent
        visited = set()

        def dfs(u, p):
            visited.add(u)
            for v in adjacency_list[u]:
                if v == p:
                    continue  # ignore the edge back to parent
                if v in visited:
                    # Found a back-edge closing a cycle: return the pair that closed it
                    return (u, v)
                parent[v] = u
                got = dfs(v, u)
                if got is not None:
                    return got
            return None

        # run DFS from some node present in edges
        start = edges[0][0]
        parent[start] = 0  # sentinel
        closing = dfs(start, 0)
        if closing is None:
            return []  # no cycle found (shouldn't happen for this problem)

        u, v = closing
        # Reconstruct the cycle: walk parents from u back to v, collect edges on the path, add (u,v)
        cycle_edges = []
        x = u
        while x != v:
            p = parent[x]
            cycle_edges.append((min(x, p), max(x, p)))
            x = p
        cycle_edges.append((min(u, v), max(u, v)))

        # Pick the edge that appeared last in input
        best = max(cycle_edges, key=lambda e: input_index[e])
        return list(best)


            


        