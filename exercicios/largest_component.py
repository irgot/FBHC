from collections import defaultdict


def exploreSize(graph, current, visiteds):
    if current in visiteds:
        return 0
    visiteds.append(current)
    size = 1
    for neighbor in graph[current]:
        size += exploreSize(graph, neighbor, visiteds)
    return size


def largestComponent(graph):
    maxCount = 0

    visiteds = list()
    for node in graph:
        count = exploreSize(graph, node, visiteds)
        maxCount = count if count > maxCount else maxCount

    return maxCount


graph = defaultdict(lambda: list())

graph[0] = [8, 1, 5]
graph[1] = [0]
graph[5] = [0, 8]
graph[8] = [0, 5]
graph[2] = [3, 4]
graph[3] = [2, 4]
graph[4] = [3, 2]


print(largestComponent(graph))
