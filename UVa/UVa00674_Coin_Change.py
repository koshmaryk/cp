import sys

MAX_V = 10001
coins = [1, 5, 10, 25, 50]
N = len(coins)
memo = [[-1] * MAX_V for _ in range(N)]

def ways(coin_type: int, value: int) -> int:
    if value == 0: # one way, use nothing
        return 1
    
    if value < 0 or coin_type == N: # invalid or done
        return 0
    
    if memo[coin_type][value] == -1: # ignore this type + one more of this type
        memo[coin_type][value] = ways(coin_type + 1, value) + ways(coin_type, value - coins[coin_type])
    
    return memo[coin_type][value]


if __name__ == '__main__':
    for line in sys.stdin:
        if line == "\n":
            break

        money = int(line)
        print(ways(0, money))
