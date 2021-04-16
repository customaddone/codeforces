from collections import defaultdict, deque, Counter
from heapq import heapify, heappop, heappush
import math
from copy import deepcopy
from itertools import combinations, permutations, product
from bisect import bisect_left, bisect_right

import sys
def input():
    return sys.stdin.readline().rstrip()
def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]

mod = 10 ** 9 + 7
MOD = 998244353
INF = float('inf')
eps = 10 ** (-10)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#############
# Main Code #
#############

"""
Consider an infinite triangle made up of layers. 何艘かの三角形を考える
(r, c): r is the number of the layer, and c is the number of the point in the layer
two direct edges. only one of the edges is activated.
It is guaranteed that all n points are distinct. n個の点は全て異なる
It is guaranteed that there is always at least one way to traverse all n points.
全ての点を横切る道が一つはできることが保証されます

activateな辺をスイッチする
進む
全ての点を通るためのコスト
上から順に点1から点2までのコストを求める
もしr + cが奇数なら今ラインに乗っている
(r + i, c + i)までフリーでいける
左向き、右向き何回でいけるか
(0, 0), (a, b)の場合は
左にa - b回右にb回進む

まず左　次に右
r + c = evenならdiff r - cのラインに乗っている
これに乗りたい
diff evenのラインから一つスイッチする時コスト1かかる
近傍のラインを見つける
見るのは左を何回か　だけでいい 同じdiffの時に限ってコストが右の分だけかかる
あとはdiff // 2の差
"""

T = getN()
for _ in range(T):
    N = getN()
    R = [1] + getList()
    C = [1] + getList()
    P = [[r, c] for r, c in zip(R, C)]
    P.sort()

    ans = 0
    for i in range(N):
        diff1 = P[i][0] - P[i][1]
        diff2 = P[i + 1][0] - P[i + 1][1]
        # how many times do you select right edges
        if diff1 == diff2 and diff1 % 2 == 0:
            ans += (P[i + 1][1] - P[i][1])
            continue
        # if you are to go the same group, you don't pay for it.
        g_a = diff1 // 2
        g_b = diff2 // 2
        ans += g_b - g_a
    print(ans)
