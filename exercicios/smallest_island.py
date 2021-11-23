from collections import defaultdict, deque


# grid = defaultdict(lambda: list())


def explore(grid, r, c, visited):
    rowInbounds = 0 <= r and r < len(grid)
    if(not rowInbounds):
        return 0
    colInbounds = 0 <= c and c < len(grid[r])
    if(not colInbounds):
        return 0

    if(grid[r][c] == 'W'):
        return 0

    if ((r, c)) in visited:
        return 0
    count = 1
    visited.append((r, c))

    count += explore(grid, r-1, c, visited)
    count += explore(grid, r+1, c, visited)
    count += explore(grid, r, c-1, visited)
    count += explore(grid, r, c+1, visited)
    return count


grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

visited = list()
count = 0
results = list()
for r in range(len(grid)):
    for c in range(len(grid[r])):
        result = explore(grid, r, c, visited)
        if result > 0:
            results.append(result)

print(min(results))
