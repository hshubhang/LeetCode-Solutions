class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)

        #generate all the neighbors for the given node
        def neighbors(node):
            ans = []
            for i in range(4):
                num = int(node[i])
                for change in [-1, 1]:
                    x = (num + change) % 10
                    ans.append(node[:i] + str(x) + node[i+1 :])
            return ans
    
        if "0000" in deadends:
            return -1

        queue = deque([("0000", 0)])
        seen.add("0000")
        while queue:
            node, step = queue.popleft()

            if node == target:
                return step

            node_neighbors = neighbors(node)
            for neighbor in node_neighbors:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor,step + 1))

        return -1
