from collections import Counter


def consistency():
    VOWELS = 'AEIOU'
    S = input()
    LENS = len(S)
    SCONSOANTS = list(filter(lambda x: x not in VOWELS, S))
    LENC = len(SCONSOANTS)
    LENV = LENS - LENC

    SVOWELS = list(filter(lambda x: x in VOWELS, S))
    mcv = Counter(SVOWELS).most_common(1)
    mcc = Counter(SCONSOANTS).most_common(1)

    CountV = (LENV-mcv[0][1])*2+(LENC) if len(mcv) > 0 else LENC

    CountC = (LENC-mcc[0][1])*2+(LENV) if len(mcc) > 0 else LENV

    response = min(CountC, CountV)
    return(response)
    # CVOWELS = len(SVOWELS)
    # CCONSOANTS = len(SCONSOANTS)
    # count.subtract(VOWELS)

    return mcc


for case in range(int(input())):
    print(f'Case #{case+1}: {consistency()}')
