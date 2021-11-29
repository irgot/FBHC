from collections import defaultdict

# fib_calculated = defaultdict(lambda: int(0))


def fib(n, memo=defaultdict(lambda: int())):
    memo[1] = 1
    memo[2] = 1
    if n <= 2:
        return memo[n]

    if n in memo:
        return memo[n]
    memo[n] = fib(n-1, memo)+fib(n-2, memo)
    return memo[n]


print(fib(50))
