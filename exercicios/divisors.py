from math import *


def div1(n):
    ans = set()
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            ans.add(i)
            ans.add(n//i)
    return(list(ans))


t = int(input())
while t:
    t -= 1
    n = int(input())
    print(f"div=", end="")
    vdiv1 = div1(n)
    print(*vdiv1)
