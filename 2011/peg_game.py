from collections import defaultdict


def peg():
    line = list(map(int, input().strip().split()))
    R, C, K, M = line[:4]
    # return (R, C, K, M)
    MP = defaultdict(lambda: defaultdict(bool))
    for t in range(0, M):
        MP[line[4+t]][line[4+t+1]] = True
    # print(MP[1])
    temp = defaultdict(lambda: defaultdict(float))
    K = K+1+K
    temp[0][K] = 1
    # temp[0][1] = 2

    # temp[1][1] = 1
    print(f"[{R},{C},{K}]")
    for r in range(1, R+1):
        for i in temp[r-1]:
            if(not MP[r][i]):
                if(i-1 >= 0):
                    temp[r][i-1] = temp[r-1][i]/2 + temp[r][i-1]
                if((i-1) < 0):
                    temp[r][i+1] = temp[r-1][i]/2 + temp[r][i+1]
                if((i+1) <= C):
                    temp[r][i+1] = temp[r-1][i]/2 + temp[r][i+1]
                if((i+1) > C):
                    temp[r][i-1] = temp[r-1][i]/2 + temp[r][i-1]
        for j in MP[r]:
            if MP[r][j]:
                temp[r+1][j] = temp[r-1][j]
            # print(j, r)
        print('=========')

        # print(temp[r-1]/2)
        # result = result/2

    # result = 1/(R-1)

    # for i in range(0, M):
    #     line[(i*2+4):(i*2+6)]

    return(temp)


for case in range(int(input())):
    print(f'Case #{case+1}: {peg()}')
