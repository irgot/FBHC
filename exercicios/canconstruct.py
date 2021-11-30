from collections import defaultdict


def canconstruct(v, l):
    # if v in memo:
    #     return memo[v]
    if v == '':
        return True
    for lvalue in l:
        if v.startswith(lvalue):
            suffix = v[len(lvalue):]
            if(canconstruct(suffix, l)):
                return True

        if v.endswith(lvalue):
            prefix = v.rsplit(lvalue, 1)[0]
            if(canconstruct(prefix, l)):
                return True
    return False


# memo = defaultdict(list)
print(canconstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(canconstruct('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(canconstruct('tenterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(canconstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeeeee',
    'eeeeee'
]))
