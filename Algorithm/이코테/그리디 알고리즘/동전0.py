import sys

n, k = map(int, input().split())

coins = list(map(int, input().split()))


cnt = 0
while True:
    for i in range(n):
        if k >= coins[n-1-i]:
            m_cnt = k//coins[n-1-i]
            k %= coins[n-1-i]
            cnt += m_cnt

    if k == 0:
        break

print(cnt)