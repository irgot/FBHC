

grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]


def exploreSize(grid, r, c, visiteds):
    rowInbounds = r >= 0 and r < len(grid)
    if(not rowInbounds):
        return 0
    colInbounds = c >= 0 and c < len(grid[r])
    if(not colInbounds):
        return 0
    if grid[r][c] == 'W':
        return 0

    if (r, c) in visiteds:
        return 0
    visiteds.append((r, c))
    size = 1
    size += exploreSize(grid, r-1, c, visiteds)
    size += exploreSize(grid, r+1, c, visiteds)
    size += exploreSize(grid, r, c-1, visiteds)
    size += exploreSize(grid, r, c+1, visiteds)
    return size


visiteds = list()
minSize = float('inf')
for r in range(len(grid)):
    for c in range(len(grid[r])):
        size = exploreSize(grid, r, c, visiteds)
        if size < minSize and size > 0:
            minSize = size
print(minSize)
