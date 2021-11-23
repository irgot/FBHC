from collections import defaultdict


def searchGraph(graph, current, values, visiteds=list()):
    if current in visiteds:
        return 0
    visiteds.append(current)
    results = list()
    value = values[current-1]
    for neighbor in graph[current]:
        results.append(searchGraph(graph, neighbor, values, visiteds))
    return max(results)+value


def gold_mine():
    N = int(input())
    C = list(map(lambda x: int(x), input().strip().split()))
    graph = defaultdict(lambda: list())
    for j in range(1, N):
        a, b = list(map(lambda x: int(x), input().strip().split()))
        graph[a].append(b)
        graph[b].append(a)
    visiteds = list()
    maxValue = searchGraph(graph, 1, C, visiteds)
    return(maxValue)


for case in range(int(input())):
    print(f"Case #{case+1}: {gold_mine()}")
