# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    """
    :type N: int(1 <= N <= 9)
    :type number: int(1 <= number <= 32000)
    :rtype: int
    """
    answer = 1
    dp = {N: 1}

    while answer <= 8:
        temp = dp.copy()
        for i, i_cnt in dp.items():
            for j, j_cnt in dp.items():
                if i_cnt + j_cnt <= 8:
                    res = [i+j, i-j, i*j, i//j]
                    for r in res:
                        if r not in temp and r > 0:
                            temp[r] = i_cnt + j_cnt
                        if r in temp and temp[r] > i_cnt + j_cnt:
                            temp[r] = i_cnt + j_cnt

        dp = temp
        answer += 1
        n = 0
        for i in range(answer):
            n += 10**i * N    
        dp[n] = answer
        if number in dp:
            return dp[number]

    return -1