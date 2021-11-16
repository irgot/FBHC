from collections import defaultdict, deque
from heapq import heappop, heappush
import heapq


def gold():
    N = int(input())
    C = list(map(lambda x: -int(x), input().strip().split()))
    adj = list()
    # adjv = defaultdict(list)

    for i in range(1, N):
        A, B = list(map(int, (input().split())))
        adj.append((A, B))

    aux = heapq
    aux = [(C[0], 1)]
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(lambda: int())
    dist[1] = C[0]
    already = list()
    while aux:
        curr, u = heappop(aux)
        already.append(u)
        if dist[u] < curr:
            continue
        for v, w in adj:
            # print(v, w, u)
            if w == u:
                a = v
                v = w
                w = a
            if v == u:
                if w in dist and dist[w] <= curr+C[w-1]:
                    continue
                if w in already:
                    continue
                dist[w] = curr+C[w-1]
                prev[w] = v
                # print(f'PUSH {w}')
                heappush(aux, (curr+C[w-1], w))

    min_dist = 0
    min_vert = 0
    for x in dist:
        if dist[x] < min_dist:
            min_dist = dist[x]
            min_vert = x

    elegible_edges = list()
    count_edges = defaultdict(lambda: int())
    for v, w in adj:
        count_edges[v] += 1
        count_edges[w] += 1

    for x in count_edges:
        if count_edges[x] == 1:
            if x not in (already):
                print(x)
    # dist = defaultdict(lambda: float('inf'))
    # dist[1] = -C[0]
    # aux = [(-C[0], 1)]

    # while aux:
    #     curr, u = heappop(aux)
    #     if dist[u] < curr:
    #         continue
    #     for v, w in adj[u]:
    #         # print(v, w)
    #         if v in dist and dist[v] <= curr+w:
    #             continue
    #         dist[v] = curr+w
    #         heappush(aux, (curr+w, v))

    return(prev)


for case in range(int(input())):
    print('Case #%d: %s' % (case+1, gold()))
