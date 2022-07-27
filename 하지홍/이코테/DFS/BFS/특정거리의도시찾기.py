from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
# [[],[2,3],[3,4],[]]

queue = deque()
queue.append((x,0)) #현재 위치랑 cnt 값

while queue:
    node, cnt = queue.popleft()
    
    if cnt == k:
        answer.append(node)
    elif cnt < k:
        for j in graph[node]:
            if not visited[j]:
                visited[j] = True
                queue.append((j, cnt+1))

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for elem in answer:
        print(elem)
        
#------------------------#
from collections import deque
import sys
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(x)