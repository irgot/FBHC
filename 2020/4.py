from collections import defaultdict


def fumes():
    [N, M] = map(int, input().strip().split(' '))
    fuel = M
    C = [list(map(int, input().strip().split())) for _ in range(N)]
    lookup = defaultdict(lambda: defaultdict(int))
    # C = list(map(int, input()))
    # C = list(map(int, input()))
    # C = list(map(int, input()))

    # C = [int(map(int, input())) for _ in range(N)]
    for i in range(len(C)):
        print(i)
    return(C)


for case in range(int(input())):
    print(f"Case #{case+1}: {fumes()}")
