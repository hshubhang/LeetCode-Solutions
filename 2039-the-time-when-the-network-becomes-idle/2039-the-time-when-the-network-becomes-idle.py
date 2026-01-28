class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:

        graph = defaultdict(list)
        for node1, node2 in edges:

            graph[node1].append(node2)
            graph[node2].append(node1)
        
        start = deque([0])
        distances = [0] * len(patience)
        distances[0] = 0
        visited = {0}

        while start:
            nodes_at_curr_level = len(start)
            for _ in range(nodes_at_curr_level):

                curr = start.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        start.append(neighbor)
                        distances[neighbor] = distances[curr] + 1

        max_time = 0
        
        for i in range(1, len(patience)):
            round_trip = distances[i] * 2

            if round_trip <= patience[i]:

                last_idle = round_trip

            else:

                last_message = ((round_trip - 1)// patience[i]) * patience[i]

                last_idle = round_trip + last_message

            max_time = max(max_time, last_idle)


        return max_time + 1



        




