# A. Odds and Ends

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
