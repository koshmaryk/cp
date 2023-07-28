# 8
# 2 1 0 2 0
# 2 2 0 3 0
# 2 3 0 5 0
# 1 4 0
# 0
# 0
# 0
# 1 6 0

def toposort(u: int) -> None:
    visited[u] = 1
    for v, w in adj[u]:
        if visited[v] == 0:
            toposort(v)
    
    ans.append(u)

if __name__ == '__main__':
    N = int(input())
    adj = [[] for _ in range(N)]
    for u in range(N):
        line = [int(x) for x in input().split(" ")]
        k = line[0]
        for i in range(k):
            v, w = line[2 * i + 1], line[2 * i + 2]
            adj[u].append((v, w))

    ans = []
    visited = [0] * N
    for u in range(N):
        if visited[u] == 0:
            toposort(u)

    ans = ans[::-1]
    print(' '.join(map(str, ans)))
    