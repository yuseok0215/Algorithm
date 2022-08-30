from collections import deque
n = int(input())
graph = [list(input()) for _ in range(n)]

def bfs(x,y):
    queue.append((x,y))
    direction = [[1,0],[-1,0],[0,-1],[0,1]]
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for next_x, next_y in direction:
            nx = x + next_x
            ny = y + next_y
            # 인덱스 범위 안에 있으면서, 같은 색이면서, 방문 안한 경우
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1  # 방문체크 후 큐에 넣음
                queue.append((nx,ny))


queue = deque()

# 적록색약 아닌 경우
visited = [[0] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:  # 아직 방문 안한 경우만 체킹
            bfs(i,j)
            cnt1 += 1

# 적록색약인 경우
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt2 += 1

print(cnt1, cnt2)