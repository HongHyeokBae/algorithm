

def solution(N):
    """
    type N: int
    rtype: int
    """ 
    if N == 1:
        return 4
    
    rec = [1, 1]
    
    for i in range(2, N):
        rec.append(rec[i-2] + rec[i-1])
    
    return rec[N-1] * 4 + rec[N-2] * 2