from collections import deque
import sys 
input = sys.stdin.readline

N, M, K, X = map(int, input().split())


def bfs(start):
    answer = []
    queue = deque()
    queue.append(start)
    visited[start] = True
    distance[start] = 0
    while queue:
        elem = queue.popleft()
        for value in graph[elem]:
            if not visited[value]:
                visited[value] = True
                queue.append(value)
                distance[value] = distance[elem] + 1
                if distance[value] == K:
                    answer.append(value)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')
    
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
distance = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    
    
bfs(X)

