# Copyright (c) 2021 kamyu. All rights reserved.
#
# Facebook Hacker Cup 2021 Qualification Round - Problem A2. Consistency - Chapter 2
# https://www.facebook.com/codingcompetitions/hacker-cup/2021/qualification-round/problems/A2
#
# Time:  O(|S|)
# Space: O(1)
#

from string import ascii_uppercase
from collections import defaultdict
from heapq import heappush, heappop


def dijkstra(adj, start):  # Time: O(|E| * log|V|), adj is a tree => O(|V| * log|V|)
    dist = defaultdict(lambda: float("inf"))
    dist[start] = 0
    min_heap = [(0, start)]
    while min_heap:
        curr, u = heappop(min_heap)
        if dist[u] < curr:
            continue
        for v, w in adj[u]:
            if v in dist and dist[v] <= curr+w:
                continue
            dist[v] = curr+w
            heappush(min_heap, (curr+w, v))
    return dist


def time_to_replace(S, dist, target):  # Time: O(|S|)
    return sum(dist[c][target] for c in S)


def consistency_chapter_2():
    S = input().strip()
    K = int(input())
    adj = defaultdict(list)
    for _ in range(K):
        A, B = list(input().strip())
        adj[A].append((B, 1))

    # Time: O(|V|^2 * log|V|) = O(1)
    dist = {x: dijkstra(adj, x) for x in ascii_uppercase}
    # print(adj)
    result = min(time_to_replace(S, dist, target)
                 for target in ascii_uppercase)
    print(list(time_to_replace(S, dist, target)
          for target in ascii_uppercase))
    return result if result != float("inf") else -1


for case in range(int(input())):
    print(float("inf"))
    print('Case #%d: %s' % (case+1, consistency_chapter_2()))
