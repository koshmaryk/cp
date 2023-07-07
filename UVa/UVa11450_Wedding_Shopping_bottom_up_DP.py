# https://onlinejudge.org/external/114/11450.pdf
MAX_gm = 20 #up to 20 garments at most and 20 models/garment
MAX_M = 200 # maximum budget is 200

if __name__ == '__main__':
    N = int(input()) 
    for _ in range(N):
        M, C = [int(x) for x in input().split(" ")]
        # the values of g are the row indices of DP table, the cache-friendly row-major traversal in a 2D array
        # reachable = [[False for _ in range(MAX_M)] for _ in range(MAX_gm)]
        reachable = [[False for _ in range(MAX_M)] for _ in range(2)]

        price = [[-1 for _ in range(MAX_gm)] for _ in range(MAX_gm)] # price[g <= 20][m <= 20]
        for g in range(C):
            s = [int(x) for x in input().split(" ")]
            price[g][0] = s[0] # store k in price[g][0]
            for k in range(1, price[g][0] + 1):
                price[g][k] = s[k]

        # initial values (base cases), using first garment g = 0
        for k in range(1, price[0][0] + 1):
            if M - price[0][k] >= 0:
                reachable[0][M - price[0][k]] = True

        # for g in range(1, C): # for each garment
        #     for b in range(0, M):
        #         if reachable[g - 1][b]:
        #             for k in range(1, price[g][0] + 1):
        #                 if b - price[g][k] > 0:
        #                     reachable[g][b - price[g][k]] = True # also reachable now

        current = 1
        for g in range(1, C):
            reachable[current] = [False for _ in range(MAX_M)] # reset row
            for b in range(0, M):
                if reachable[1 - current][b]:
                    for k in range(1, price[g][0] + 1):
                        if b - price[g][k] >= 0:
                            reachable[current][b - price[g][k]] = True
            current = 1 - current # IMPORTANT technique: flip the two rows


        b = 0
        while (b <= M and not reachable[1 - current][b]):
            b += 1

        if (b == M + 1):
            print("no solution")
        else:
            print(str(M - b))