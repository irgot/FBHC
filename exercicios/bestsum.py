from collections import defaultdict
from heapq import heappop, heappush


# def bestSum(n, l):
#     aux = deque()
#     aux2 = list()
#     aux.append((n, aux2))

#     while aux:
#         # aux2.clear()
#         current, aux2 = aux.popleft()
#         a = aux2.copy()
#         # print(aux2)
#         if current == 0:
#             return (a)
#         if current < 0:
#             continue
#         newaux2 = deque()

#         for value in l:
#             newaux2.clear()
#             newaux2 = a+[value]
#             # newaux2.append(value)
#             aux.append((current-value, newaux2.copy()))
#     return(None)


def bestSum(n, l, memo=defaultdict(list)):
    if n in memo:
        return memo[n]
    if n == 0:
        return[]
    if n < 0:
        return None
    shortestcombination = list()
    for value in l:
        result = bestSum(n-value, l, memo.copy())
        if result != None:
            if(len(result) < len(shortestcombination)) or len(shortestcombination) == 0:
                shortestcombination = result
    if len(shortestcombination) > 0:
        memo[n] = shortestcombination
    else:
        memo[n] = None
    return memo[n]


# teste = defaultdict(list)
memo = defaultdict(list)
# heappush(teste[1], [0, 2, 3])
# heappush(teste[1], [4, 3])
# heappush(teste[1], [7])
# heappush(teste[1], None)


print(bestSum(7, [5, 3, 4, 7], memo.copy()))
print(bestSum(8, [2, 3, 5, 7], memo.copy()))
print(bestSum(8, [1, 4, 5], memo.copy()))
print(bestSum(100, [1, 2, 5, 25], memo.copy()))
