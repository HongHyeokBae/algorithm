from collections import deque

class Solution:
    # DFS solution
    def canFinish(self, numCourses, prerequisites):
        """
        type numCourses: int
        type prerequiesties: List[List[int]]
        rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for elm1, elm2 in prerequisites:
            graph[elm1].append(elm2)  

        for root in range(numCourses):
            if not visited[root]:
                stack = [root]
                visited[root] = 1
            
            while stack:
                curr = stack.pop()

                for i in graph[curr]:
                    if i in stack:
                        return False
    
                    if not visited[i]:
                        visited[i] = 1
                        stack.append(curr)
                        stack.append(i)
                        break
    

        return True

    # BFS topological sort solution
    def canFinish_sol2(self, numCourses, prerequiesties):
        graph = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]

        for i, j in prerequiesties:
            graph[i].append(j)
            indegrees[j] += 1

        s = deque([idx for idx, ind in enumerate(indegrees) if ind == 0])
        visited = []

        while s:
            n = s.popleft()
            visited.append(n)

            for m in graph[n]:
                indegrees[m] -= 1
                if indegrees[m] == 0:
                    s.append(m)

        return len(visited) == numCourses

        

        