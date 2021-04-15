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
denote: 示す
約数の和がcになる値を出せ
c <= 10,000,000 なので全種類出すのは調和級数でも無理そう

で通る　それはそう
tは小さいのでこれでなんとか

素数は1 + 素数
2で割れるなら 1 + 2 + 素数
全ての
約数の総和は(1 + 2 + 2^2) * (1 + 3 + 3^2) * ...みたいにやる
cの素因数分解は間に合う
それぞれの因数について(1 + n + n^2...)の形で表現できるか

まず1を引いた数は素数ですか？　いいえ

"""

lim = 10 ** 7 + 7
l = [1] * lim
for i in range(2, lim):
    j = i
    while j < lim:
        l[j] += i
        j += i

ans = [-1] * lim
for i in range(lim - 1, 0, -1):
    if l[i] < lim:
        ans[l[i]] = i

T = getN()
for _ in range(T):
    c = getN()
    print(ans[c])
