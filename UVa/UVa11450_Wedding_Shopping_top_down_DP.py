# https://onlinejudge.org/external/114/11450.pdf
MAX_gm = 20 #up to 20 garments at most and 20 models/garment
MAX_M = 200 # maximum budget is 200

# the current garment g and the current budget left b
def dp(g: int, b: int) -> int:
    if b < 0:
        return -1e9 # fail, return -ve number

    if g == C:
        return M - b # we are done
    
    # if the line below is commented, top-down DP will become backtracking!!
    if memo[g][b] != -1: # top-down memoization
        return memo[g][b]

    ans = -1 # start with a -ve number
    for k in range(1, price[g][0] + 1):
        ans = max(ans, dp(g + 1, b - price[g][k])) # try each model k
    memo[g][b] = ans # top-down: memoize ans
    return ans

if __name__ == '__main__':
    N = int(input()) 
    for _ in range(N):
        M, C = [int(x) for x in input().split(" ")]
        memo = [[-1] * MAX_M for _ in range(MAX_gm)] # top-down: init memo

        price = [[-1] * MAX_gm for _ in range(MAX_gm)]
        for g in range(C):
            s = [int(x) for x in input().split(" ")]
            price[g][0] = s[0] # store k in price[g][0]
            for k in range(1, price[g][0] + 1):
                price[g][k] = s[k]

        ans = dp(0, M)
        if ans < 0:
            print("no solution\n")
        else:
            print("{}\n".format(ans))
