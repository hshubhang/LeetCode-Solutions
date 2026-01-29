class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #add deadends in a visited set
        seen = set(deadends)
        queue = deque(["0000"])
        def neighbors(node):
            ans = []
            for i in range(4):
                number = int(node[i])

                for change in [-1,1]:
                    x = (number + change) % 10
                    ans.append(node[:i] + str(x) + node[i+1 :])

            return ans
        #basecase
        if "0000" in deadends:
            return -1

        steps = 0
        while queue:
            
            nodes_on_curr_level = len(queue)
            for _ in range(nodes_on_curr_level):

                node = queue.popleft()

                if node == target:
                    return steps

                for neighbor in neighbors(node):

                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)


            steps += 1
                    
            
            
        return -1





