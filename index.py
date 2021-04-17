class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (N + 1)
        self.b = 1 << N.bit_length() - 1

    def add(self, a, w):
        x = a
        while(x <= self.N):
            self.bit[x] += w
            x += x & -x

    def get(self, a):
        ret, x = 0, a - 1
        while(x > 0):
            ret += self.bit[x]
            x -= x & -x
        return ret

    def cum(self, l, r):
        return self.get(r) - self.get(l)

N, M = map(int, input().split())
event = []
for i in range(M):
    s, g = map(int, input().split())
    event.append([s, 0, 0])
    event.append([g, s, 1])
event.sort(reverse = True)

bit = BIT(N)
ans = 0

# 1-indexのBITを使うので1から
for i in range(1, N + 1):
    close = []
    while event and event[-1][0] <= i:
        _, s, dir = event.pop()
        # ここが終点
        if dir == 1:
            close.append(s)
        # ここが始点
        else:
            # 始点を立てる
            bit.add(i, 1)

    # ここが終点であるものを始点が近いものから処理する
    close.sort()
    while close:
        # 自身の始点 + 1 ~ 終点 - 1まで[s + 1, i)に他の始点がいくつあるか
        s = close.pop()
        ans += bit.cum(s + 1, i)
        # 始点を消す
        bit.add(s, -1)

print(ans)
