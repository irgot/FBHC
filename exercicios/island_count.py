from collections import defaultdict, deque


# grid = defaultdict(lambda: list())


def explore(grid, r, c, visited):
    rowInbounds = 0 <= r and r < len(grid)
    if(not rowInbounds):
        return False
    colInbounds = 0 <= c and c < len(grid[r])
    if(not colInbounds):
        return False

    if(grid[r][c] == 'W'):
        return False

    if (r, c) in visited:
        return False

    visited.append((r, c))

    explore(grid, r-1, c, visited)
    explore(grid, r+1, c, visited)
    explore(grid, r, c-1, visited)
    explore(grid, r, c+1, visited)
    return True


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
for r in range(len(grid)):
    for c in range(len(grid[r])):
        count += 1 if explore(grid, r, c, visited) else 0

print(count)
