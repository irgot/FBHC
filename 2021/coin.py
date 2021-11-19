from collections import defaultdict


def f(indx, val):
    if(val < 0):
        return float('inf')
    if(indx >= len(S)):
        return val
    if(memo[indx][val] == float('inf')):
        memo[indx][val] = min(1+f(indx, val-S[indx]), f(indx+1, val))

    return memo[indx][val]


for case in range(int(input())):
    print('Case #%d: ' % (case+1), end="")
    memo = defaultdict(lambda: defaultdict(lambda: float('inf')))
    V = int(input())
    S = list(map(lambda x: int(x), input().strip().split()))
    print(f(0, V))
