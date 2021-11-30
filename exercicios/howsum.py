from collections import defaultdict


def howSum(n, l, memo=defaultdict(list)):
    if n == 0:
        return ([])
    if n in memo:
        return memo[n]
    if n > 0:
        for lvalue in l:
            remainder = n - lvalue
            result = howSum(remainder, l, memo)
            if result != None:
                memo[n] = result+[lvalue]
                return memo[n]
    memo[n] = None
    return memo[n]


memo = defaultdict(list)

print(howSum(7, [5, 3, 4, 7], memo))
memo.clear()
print(howSum(7, [2, 3], memo))
memo.clear()
print(howSum(7, [2, 4], memo))
memo.clear()
print(howSum(8, [2, 3, 5, 7], memo))
memo.clear()
print(howSum(300, [7, 14], memo))
memo.clear()
