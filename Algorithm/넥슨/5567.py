from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline



def bfs(start):
    cnt = 0
    visited = [0]* (N+1)
    visited[start] = 1
    queue = deque()
    queue.append([start, 0])
    
    while queue:
        u, dist = queue.popleft()
        if dist <= 2:
            cnt += 1
        for elem in graph[u]:
            if visited[elem] == 0:
                visited[elem] == 1
                queue.append([elem, dist+1])
    return cnt - 1
                

    
N = int(input())
M = int(input())

graph=[[] for _ in range(M+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print(bfs(1))