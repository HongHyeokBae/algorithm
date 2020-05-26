from collections import deque

class Solution:
    def routeBetweenNodes(self, graph, start, end):
        """
        type graph: List[List[int]]
        start: int
        end: int
        rtype: bool
        """
        visited, q = [0] * len(graph), deque()
        q.append(start)
        visited[start] = 1
        
        while q:
            parent = q.popleft()
            if parent == end:
                return True

            for child in graph[parent]:
                if visited[child] == 0:
                    q.append(child)
                    visited[child] = 1
        
        return False