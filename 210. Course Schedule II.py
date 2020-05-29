from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        type numCourses: int
        type prerequisties: List[List[int]]
        rtype: List[int]
        """
        indegrees = [0] * numCourses
        adjList = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            indegrees[edge[0]] += 1
            adjList[edge[1]].append(edge[0])
        
        zeroIndVertex = deque([idx for idx, ind in enumerate(indegrees) if ind == 0])
        order = []

        while zeroIndVertex:
            v = zeroIndVertex.popleft()
            order.append(v)

            for vertex in adjList[v]:
                indegrees[vertex] -= 1
                if indegrees[vertex] == 0:
                    zeroIndVertex.append(vertex)
        
        return order if len(order) == numCourses else []