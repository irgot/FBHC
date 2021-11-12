

teste = [[1], [2], [3], [4], [5]]

teste.sort()


for direction in (lambda x: x, reversed):
    for t in direction(teste):
        print(f't => {t}')
