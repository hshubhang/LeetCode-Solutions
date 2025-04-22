class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for courses, prerequ in prerequisites:
            graph[prerequ].append(courses)

        print(graph)

        indegree = {i: 0 for i in range(numCourses)}

        print(indegree)

        for prerequ, courses in graph.items():
            for course in courses:
                indegree[course] += 1

        queue = deque()

        for course, degree in indegree.items():
            if degree == 0:
                queue.append(course)
        
        while queue:
            curr_course = queue.popleft()
            for depen in graph[curr_course]:
                indegree[depen] -= 1
                if indegree[depen] == 0:
                    queue.append(depen)

        return all(degree == 0 for degree in indegree.values())


        