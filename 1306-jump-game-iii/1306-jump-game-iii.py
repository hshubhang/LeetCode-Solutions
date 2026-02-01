class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start >= len(arr):
            return False


        queue = deque([start])
        visited = {start}


        while queue:

            curr_node_index = queue.popleft()

            if arr[curr_node_index] == 0:
                return True

            for change in [curr_node_index - arr[curr_node_index], curr_node_index + arr[curr_node_index]]:
                if change in visited or change >= len(arr) or change < 0:
                    continue

                else:
                    visited.add(change)
                    queue.append(change)

        
        return False

            

