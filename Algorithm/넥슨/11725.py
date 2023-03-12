from collections import deque
import sys
sys.setrecursionlimit(10*9)
def bfs():
    tmp = que.popleft()
    for value in graph[tmp]:
        if result[value] == 0:
            result[value] == tmp
            que.append(value)
            bfs()
            
        
N = int(input())

graph = [[] for _ in range(N+1)]
result = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)
    
    
que = deque()
que.append(1)

bfs()
ans = result[2:]
for elem in ans:
    print(elem)





