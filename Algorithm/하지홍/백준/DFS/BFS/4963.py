from collections import deque

# 동 동남 남 남서 서 북서 북
d_x = [0,1,1,1,0,-1,-1,-1]
d_y = [1,1,0,-1,-1,-1,0,1]

def bfs(graph, a, b):
    queue = deque()
    graph[a][b] = 0
    queue.append((a, b))
 
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + d_x[i]
            ny = y + d_y[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 2
                queue.append((nx, ny))
 
 
while True:
    w, h = map(int, input().split())
    graph = []
    if w == 0 and h == 0:
        break
    for i in range(h):
        graph.append(list(map(int, input().split())))
 
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1
    print(cnt)