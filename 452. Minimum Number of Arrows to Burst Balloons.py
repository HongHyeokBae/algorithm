

class Solution:
    def findMinArrowShots(self, points):
        """
        type points: List[List[int]]
        rtype: int
        """
        shots, arrow = 0, float('-inf')
        
        points.sort(key = lambda point: point[1])
        
        for point in points:
            if arrow < point[0]:
                arrow = point[1]
                shots += 1
                
        return shots
        