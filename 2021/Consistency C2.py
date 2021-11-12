from collections import Counter, defaultdict, deque
from string import ascii_uppercase


def findBestPath(s, t, ct, tc, listauxs, listauxt):
    # T ->
    #B - A
    #s - t

    # print(f'fs {s} - ft {t} - ct {ct}')

    count = 1
    dd = defaultdict(lambda: defaultdict(int))
    if t in ct[s]:
        # print(f't {t} in ct[s] {ct[s]}')
        return count
    # if len(ct[s]) == 0:
    #     return -1
    # if len(tc[t]) == 0:
    #     return -1
    else:
        results = deque()
        results.clear()
        for ssub in ct[s]:

            if ssub in listauxs and t in listauxt:
                continue
            # print(ssub, t)
            listauxs.append(ssub)
            listauxt.append(t)
            if not dd[ssub][t]:
                count2 = findBestPath(
                    ssub, t, ct, tc, listauxs, listauxt)
                dd[ssub][t] = count2
            else:
                count2 = dd[ssub][t]

            results.append(count2)
        if len(results) > 0:
            if len(list(filter(lambda x: x != -1, results))) > 0:
                mini = min(filter(lambda x: x != -1, results))
                count = mini+count
                print(s, t, count)
                return(count)
            else:
                return(-1)
        else:
            return(-1)
    return(-1)


def consistency():
    # VOWELS = 'AEIOU'+'asdf'
    S = input()
    K = int(input())

    LL = deque()
    LA = deque()
    LT = deque()
    ct = defaultdict(str)
    tc = defaultdict(str)
    for i in (range(0, K)):
        LL.append(input())
        ct[LL[i][0]] = LL[i][1]+ct[LL[i][0]]
        tc[LL[i][1]] = LL[i][0]+tc[LL[i][1]]
        # LA.append(LL[i][0])
        # LT.append(LL[i][1])
    fullS = S
    # fullS = ascii_uppercase
    for s in tc:
        fullS += s
    countLetters = Counter(fullS).most_common()
    count = defaultdict(lambda: defaultdict(int))
    # print(findBestPath('A', 'Z', ct, tc))
    som = 0
    initial = 1
    results = deque()
    # c = findBestPath('O', 'X', {'N': 'XI', 'O': 'IE', 'E': 'W', 'F': 'NE', 'X': 'W', 'I': ''}, {
    #     'I': 'ON', 'E': 'FO', 'X': 'N', 'W': 'XE', 'N': 'F', 'F': '', 'O': ''})
    # return '1'
    for t in countLetters:
        som = 0
        for s in S:
            if t[0] == s:
                continue

            # count[t[0]][s] = findBestPath(s, t[0], ct, tc)
            # print(f'{s}-{t[0]}')
            c = findBestPath(s, t[0], ct, tc, deque(), deque())
            # print(f'{s}-{t[0]}=>c={c}')
            # print(f'tc={tc}')
            if c > 0:
                som += c
            else:
                som = -1
                break
        results.append(som)

    # print(i[0])
    # for k in (temp):
    #     for i in (temp):
    #         for j in temp[i]:
    # return('a')
    # return(results)
    x = list(filter(lambda x: x != -1, results))
    if len(x) == 0:
        result = -1
    else:
        result = min(x)
    return(results)


for case in range(int(input())):
    print(f'Case #{case+1}: {consistency()}')
