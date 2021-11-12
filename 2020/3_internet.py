from collections import defaultdict


def timber():
    N = int(input())
    P = [list(map(int, input().strip().split())) for _ in range(N)]
    P.sort()
    # print(P)
    lookup = defaultdict(lambda: defaultdict(int))

    result = 0
    for d, direction in ((1, lambda x: x), (-1, reversed)):
        # print(d, direction)
        for p, l in direction(P):
            # print(d, p, l, p+d*l)
            lookup[d][p+d*l] = max(lookup[d][p+d*l], lookup[d][p]+l)
        for p, l in lookup[d].items():
            result = max(result, lookup[-d][p]+l)
    print(lookup)
    return result


for case in range(int(input())):
    print('Case #%d: %s' % (case+1, timber()))
