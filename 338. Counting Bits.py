class Solution:
    # number of 1 bit for 2, 4, 8, ... is always 1
    # if n is bin < n < bin * 2, dp[n] = 1(dp[bin]) + dp[n - bin]
    # ex) 
    # 5 = 4 + 1 (101 = 100 + 1)
    # 6 = 4 + 2 (110 = 100 + 10)
    # 7 = 4 + 3 (111 = 100 + 11)

    def countBits(self, num: int):
        bin, res = 1, [0]
        
        for i in range(1, num + 1):
            if i == bin:
                bin = bin * 2
                res.append(1)
            else:
                print(bin ,i)
                res.append(1 + res[i - bin])

        return res