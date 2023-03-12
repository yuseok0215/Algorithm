from collections import deque
n, k = map(int, input().split())
visited = [0 for i in range(100001)]

def bfs(a, visited):
    queue = deque()
    queue.append(a)
    
    while queue:
        b = queue.popleft()
        if b == k:
            return visited[b]
        for next_b in (b-1, b+1, b*2):
            if 0 <= next_b < 100001 and not visited[next_b]:
                queue.append(next_b)
                visited[next_b] = visited[b] + 1
                
print(bfs(n,visited))