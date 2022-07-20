from collections import deque
from operator import ne

n, m, k, x = map(int, input().split())

arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b =  map(int, input().split(' '))  
    arr[a].append(b)
    
dist = [-1] * (n+1)
dist[x] = 0

queue = deque([x])
while queue:
    n = queue.popleft()

    for next in arr[n]:
        if dist[next] == -1:
            dist[next] = dist[n] + 1
            queue.append(next)

if k in dist:
    for i in range(1, n+1):
        if dist[i] == k:
            print(i)
            
else:
    print(-1)

    
