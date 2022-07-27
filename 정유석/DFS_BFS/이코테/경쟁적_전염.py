n, k = map(int, input().split()) # 맵크기, 바이러스 종류

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def virus(x, y, k):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] == k
                # virus(nx, ny, k)

time = 0
cnt = 0

def bfs(s, x, y):
    global time
    global cnt
    
    # 바이러스 증식
    for i in range(n):
        for j in range(n):
            for m in range(k):
                if graph[i][j] == m+1: # 1, 2, 3
                    virus(i, j, m+1)
    
    # 맵이 바이러스로 꽉 찼을 때 끝내거나
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                cnt += 1
    
    if cnt != 0:
        return graph[x-1][y-1]
    # 시간이 다 됐을 때 끝내거나
    
    time += 1
    if time == s:
        return graph[x-1][y-1]

    

target_virus = bfs(s, x, y)
print(target_virus)