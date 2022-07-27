from collections import deque # bfs에서는 참거짓을 지양

dx=[-1,0,1,0,1,-1,1,-1]
dy=[0,1,0,-1,1,1,-1,-1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    
    while q:
        a, b = q.popleft()
        
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<=nx<h and 0<=ny<w:
                if graph[nx][ny] != 0:
                    graph[nx][ny] = 0
                    q.append((nx, ny))

result = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h ==0:
        break

    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    land_cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                land_cnt += 1 # 섬 개수 처음에 하나 늘려주고
                bfs(i, j) # 붙어있는 땅들을 다 0으로 만들어주자.
    
    result.append(land_cnt)

for i in range(len(result)):
    print(result[i])




