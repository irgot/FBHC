from collections import defaultdict, deque


def edgeToGraph(edges):
    graph = defaultdict(lambda: list())
    for edge in edges:
        A, B = edge
        graph[A].append(B)
        graph[B].append(A)
    return graph


def bft(graph, start, nodeB):
    # count = 1
    # if current == nodeB:
    #     return count
    # if current in visiteds:
    #     return 0
    # visiteds.append(current)
    # for neighbor in graph[current]:
    #     count += bft(graph, neighbor, nodeB, visiteds)
    # return count
    queue = deque()
    queue.append((start, 0))
    visiteds = list()
    while queue:
        current, distance = queue.popleft()
        if current == nodeB:
            return distance
        # if current in visiteds:
        #     continue
        visiteds.append(current)
        for neighbor in graph[current]:
            if neighbor in visiteds:
                continue
            queue.append((neighbor, distance+1))
    return(-1)


def smallestPath(edges, nodeA, nodeB):
    graph = edgeToGraph(edges)
    smallest = bft(graph, nodeA, nodeB)
    return(smallest)


edges = list()
edges.append(['w', 'x'])
edges.append(['x', 'y'])
edges.append(['z', 'y'])
edges.append(['z', 'v'])
edges.append(['w', 'v'])

print(smallestPath(edges, 'w', 'a'))
