from collections import defaultdict


def allconstruct(target, wordbank, memo=defaultdict(list)):
    if target in memo:
        return memo[target]
    if(target == ''):
        return [[]]
    results = [[]]
    results.clear()
    targetways = []
    for word in wordbank:
        if target.startswith(word):
            targetways.clear()
            suffix = target[len(word):]
            suffixways = allconstruct(suffix, wordbank, memo)
            targetways = list(map(lambda x: [word]+x, suffixways))
            # print(targetways)
            results += targetways.copy()
    memo[target] = results.copy()
    return memo[target]


memo = defaultdict(list)
print(allconstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], memo.copy()))
print(allconstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], memo.copy()))
print(allconstruct('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], memo.copy()))
print(allconstruct('tenterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't'], memo.copy()))
print(allconstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeeeee',
    'eeeeee'
], memo.copy()))
