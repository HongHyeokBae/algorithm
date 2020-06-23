

def solution(triangle):
    """
    type triangle: List[List[int]]
    rtype: int
    """
    
    maxLevel = len(triangle) - 1
    
    for level in range(maxLevel - 1, -1, -1):
        for i in range(len(triangle[level])):
            triangle[level][i] = triangle[level][i] + max(triangle[level+1][i], triangle[level+1][i+1])
        
        print(triangle)
            
    return triangle[0][0]