class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        ans = []
        for node, neighbor in edges:
            graph[node].append(neighbor)
        
        set_of_vals = set()
        for edge in graph.values():
            for item in edge:
                set_of_vals.add(item)

        for i in range(n):
            if i not in set_of_vals:
                ans.append(i)

        return ans