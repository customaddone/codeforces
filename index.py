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

sys.setrecursionlimit(1000000000)
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
# 奇数の長さの奇数で始まり奇数で終わる数列に分割する
# 奇数個の数列にできるか

# 偶数は抱き込む必要がある
もちろんDP 長さ100か
dp[i][j]: i - 1まで進んだ時にj個分割した
"""

N = getN()
A = getList()

dp = [set() for i in range(N + 1)]
dp[0].add(0)

for i in range(N):
    if A[i] % 2 == 0:
        continue
    # 次に飛べるとこ
    for j in range(i, N):
        for o in list(dp[i]):
            # 次に飛ぶとこが奇数かつ長さが奇数
            if A[j] % 2 == 1 and (j - i) % 2 == 0:
                dp[j + 1].add(o + 1)

for o in list(dp[N]):
    if o % 2 == 1:
        print('Yes')
        exit()

print('No')
