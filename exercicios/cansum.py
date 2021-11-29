from collections import defaultdict


def canSum(n, l=list(), memo=defaultdict(int)):
    results = list()
    if n == 0:
        return True
    if n in memo:
        return memo[n]
    if n > 0:
        for lvalue in l:
            memo[n] = canSum(n-lvalue, l, memo)
            if(memo[n]):
                return(True)
        pass
    memo[n] = False
    return False


# def camSum(targetSum, numbers=list()):


print(canSum(300, [7, 14]))
