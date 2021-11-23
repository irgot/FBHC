from collections import defaultdict
from heapq import heappush, heappop


def dfs(adj, C, parent, curr):
    min_heap, cnt = [], 2 if not curr else 1
    for child in adj[curr]:
        if child == parent:
            continue
        heappush(min_heap, dfs(adj, C, curr, child))
        if len(min_heap) > cnt:
            heappop(min_heap)
        print(min_heap)
    return C[curr]+sum(min_heap)


def gold_mine_chapter_1():
    N = int(input())
    # C = list(map(lambda: int, input().strip().split()))
    C = list(map(lambda x: int(x), input().strip().split()))
    # adj = [[] for _ in range(N)]
    adj = defaultdict(lambda: list())
    for _ in range(N-1):
        A, B = list(map(lambda x: int(x)-1, input().strip().split()))
        adj[A].append(B)
        adj[B].append(A)

    return dfs(adj, C, -1, 0)


for case in range(int(input())):
    print('Case #%d: %s' % (case+1, gold_mine_chapter_1()))
