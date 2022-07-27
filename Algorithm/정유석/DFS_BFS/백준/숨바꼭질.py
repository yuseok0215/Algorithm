from collections import deque

from sympy import Max

n, k = map(int, input().split())
Max = 1000000
dist = [0] * (Max+1)


def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break

        for i in (x-1, x+1, x*2): # 갈 수 있는 거리를 모두 체크해서 최종 값 찾기
            if 0<= i <= Max and not dist[i]:
                dist[i] = dist[x] + 1
                q.append(i)


bfs()
    