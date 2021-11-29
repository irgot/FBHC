from collections import defaultdict


def grid_traveler(r, c, memo=defaultdict(lambda: int())):
    if memo[(r, c)]:
        return memo[(r, c)]
    if memo[(c, r)]:
        return memo[(c, r)]

    if((r, c) == (1, 1)):
        return 1
    if(r == 0 or c == 0):
        return 0
    memo[(r, c)] = grid_traveler(r, c-1, memo)+grid_traveler(r-1, c, memo)
    return memo[(r, c)]


print(grid_traveler(1, 1))
print(grid_traveler(2, 3))
print(grid_traveler(3, 2))
print(grid_traveler(3, 3))
print(grid_traveler(18, 18))
