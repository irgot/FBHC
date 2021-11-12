import logging
import sys
sys.setrecursionlimit(8000000)


def maptree_r(tree, pi, pf):
    if(tree[0] == pf or tree[0]+tree[1] == pi):
        return True
    else:
        return False


def maptree_l(tree, pi, pf):
    if(tree[0] == pi or tree[0]-tree[1] == pf):
        return True
    else:
        return False


def paths(trees, pi, pf):
    l_p = 0
    r_p = 0
    # logging.warning(len(trees))

    p_trees_r = list(filter(lambda tree: maptree_r(tree, pi, pf), trees))

    p_trees_l = list(filter(lambda tree: maptree_l(tree, pi, pf), trees))

    for i in range(len(p_trees_r)):
        # right

        # trees_c.pop(i)

        # print('R ', pi, pf, p_trees_r[i], '=>', pf-pi)
        trees = list(filter(lambda tree: not tree in p_trees_r, trees))
        l_p = paths(trees, min(p_trees_r[i][0], pi),
                    max(p_trees_r[i][0]+p_trees_r[i][1], pf))  # right
        # r_p = paths(trees_c.copy(), min(trees[i][0] -
        #             trees[i][1],pi), max(trees[i][0],pf))  # left
        # trees.pop(i)

    for i in range(len(p_trees_l)):

        # trees = trees[i+1:].copy()
        # trees_c.pop(i)
        # l_p = paths(trees_c.copy(), trees[i][0],
        #             trees[i][0]+trees[i][1])  # right
        # print('L ', pi, pf, p_trees_l[i], '=>', pf-pi)
        trees = list(filter(lambda tree: not tree in p_trees_l, trees))
        r_p = paths(trees, min(p_trees_l[i][0] -
                               p_trees_l[i][1], pi), max(p_trees_l[i][0], pf))  # left
    # R  5 39 [-6, 11] => 34
        # trees.pop(i)
    # print(f'pi - pf =>{pi} {pf} = {pf-pi} return={max(l_p, r_p, (pf-pi))}')
    # l_p.append(0)
    # r_p.append(0)
    # max_lp = max(l_p)
    # max_rp = max(r_p)
    # print(f'max_lp & rp => ({l_p} , {r_p},{pi} {pf} = , {pf-pi})')

    aws = max(l_p, r_p, (pf-pi))

    return(aws)


with open('timber_input.txt') as f:
    lines = f.read().split('\n')
    case = 0
    for l in range(1, len(lines)):
        if (lines[l].count(' ') == 0 and len(lines[l]) > 0):
            # print(l)

            case = case+1
            nt = int(lines[l])
            # logging.warning(f'nt=>{nt}')
            trees = []
            trees_sorted_r = []
            trees_sorted_l = []
            for t in range(0, nt):
                # print(f"t=>{t} l=>{l} l+t+1=>{l+t+1}")
                tree = list(map(lambda x: int(x), lines[l+t+1].split(' ')))
                trees.append(tree.copy())
            trees_sorted_r = sorted(trees, key=lambda d: d[0])
            trees_sorted_l = sorted(trees, key=lambda d: d[0]-d[1])

            # p_trees_l = list(
            #     map(lambda tree: [tree[0]-tree[1], tree[0]], trees))
            # p_trees_r = list(
            #     map(lambda tree: [tree[0], tree[0]+tree[1]], trees)
            # )
            l_p = []
            r_p = []

            # for i in (range(len(trees_sorted_r))):
            #     logging.warning(i)
            #     trees_c = trees_sorted_r[i+1:].copy()
            #     # trees_c.pop(i)

            #     r_p.append(paths(trees_c.copy(), trees_sorted_r[i][0],
            #                      trees_sorted_r[i][0]+trees_sorted_r[i][1]))
            #     # right
            # for i in (range(len(trees_sorted_l))):
            #     logging.warning(i)
            #     trees_c = trees_sorted_l[i+1:].copy()
            #     l_p.append(paths(trees_c.copy(), trees[i][0] -
            #                      trees[i][1], trees[i][0]))  # left

            # trees.pop(i)
            # print()
            result_r = paths(
                trees_sorted_r[1:], trees_sorted_r[0][0], trees_sorted_r[0][0] + trees_sorted_r[0][1])

            result_l = paths(
                trees_sorted_l[1:], trees_sorted_l[0][0]-trees_sorted_l[0][1], trees_sorted_l[0][0])

            # max_lp = max(l_p)
            # max_rp = max(r_p)
            # logging.warning(f"Case  # {case}: {max(max_lp, max_rp)}")
            print(f"Case #{case}: {max(result_r,result_l)}")
            # print(max(3, 5, 1+9))
            # print(t)
            #     tree_d = {'size': int(tree[1]), 'sr': int(tree[0]), 'er': int(
            #         tree[0])+int(tree[1]), 'sl': int(tree[0])-int(tree[1]), 'el': int(tree[0])}
            #     trees.append(tree_d.copy())
            # print(trees)
            # trees_c = sorted(trees, key=lambda d: d['size'], reverse=True)

            # mlott = 0
            # maxsize = 0
            # for i in range(0, len(trees_c)):
            #     sr = trees_c[i]['sr']
            #     sl = trees_c[i]['sl']
            #     er = trees_c[i]['er']
            #     el = trees_c[i]['el']
            #     size = trees_c[i]['size']
            #     trees_c2 = trees_c.copy()
            #     lpr = trees_c[i]['er']
            #     lpl = trees_c[i]['el']
            #     ind = 0
            #     maxlpr = lpr-sr
            #     maxlpl = lpl-sl
            #     maxsize = maxsize if maxsize > size else size
            #     trees_c2.pop(i)
            #     while ind < len(trees_c2):
            #         sr_c = trees_c2[ind]['sr']
            #         sl_c = trees_c2[ind]['sl']
            #         er_c = trees_c2[ind]['er']
            #         el_c = trees_c2[ind]['el']
            #         size_c = trees_c2[ind]['size']

            #         if sr_c == lpr:
            #             lpr = er_c
            #             print(f'er_c = {er_c}')
            #             maxlpr = lpr-sr
            #             trees_c2.pop(ind)
            #             ind = 0
            #             maxsize = maxsize if maxsize > maxlpr else maxlpr
            #             continue
            #         if sl_c == lpr:
            #             lpr = el_c
            #             print(f'el_c = {el_c}')
            #             maxlpr = lpr-sr
            #             trees_c2.pop(ind)

            #             maxsize = maxsize if maxsize > maxlpr else maxlpr
            #             ind = 0
            #             continue
            #         if sr_c == lpl:
            #             lpl = er_c
            #             print(f'er_c = {er_c}')
            #             maxlpl = lpl-sl
            #             trees_c2.pop(ind)

            #             maxsize = maxsize if maxsize > maxlpl else maxlpl
            #             ind = 0
            #             continue
            #         if sl_c == lpl:
            #             print(f'el_c = {el_c}')
            #             lpl = el_c
            #             maxlpl = lpl-sl
            #             trees_c2.pop(ind)

            #             maxsize = maxsize if maxsize > maxlpl else maxlpl
            #             ind = 0
            #             continue

            #         ind = ind+1
            # print(f"Case #{case}: {trees_sorted}", end="")
            # print(maxsize)
