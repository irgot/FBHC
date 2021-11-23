from collections import defaultdict, deque


def connected_count(graph):
    visiteds = list()
    count = 0
    for node in graph:
        if (explore(graph, node, visiteds)):
            count += 1
    return count


def explore(graph, current, visiteds=list()):
    if current in visiteds:
        return False
    visiteds.append(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, visiteds)
    return True


graph = defaultdict(lambda: list())

graph[0] = [8, 1, 5]
graph[1] = [0]
graph[5] = [0, 8]
graph[8] = [0, 5]
graph[2] = [3, 4]
graph[3] = [2, 4]
graph[4] = [3, 2]

print(connected_count(graph))
