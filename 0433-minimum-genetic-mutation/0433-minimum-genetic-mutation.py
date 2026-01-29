class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        

        seen = {startGene}
        print(seen)
        def neighboring_genes(node):
            ans = []
            for i in range(8):
                for new_char in ["A", "C", "G", "T"]:
                    if new_char != node[i]:
                        new_string = node[:i] + new_char + node[i+1:]
                        if new_string in bank:
                            ans.append(new_string)

            
            return ans
        
        queue = deque([startGene])
        steps = 0
        while queue:
            nodes_at_curr_level = len(queue)

            for _ in range(nodes_at_curr_level):
                
                node = queue.popleft()

                if node == endGene:
                    return steps

                
                for neighbor in neighboring_genes(node):
                    if neighbor not in seen and neighbor in bank:
                        seen.add(neighbor)
                        queue.append(neighbor)

            
            steps += 1

        return -1
    



