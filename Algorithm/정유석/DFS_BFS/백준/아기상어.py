from collections import deque

from regex import E

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

shark_x, shark_y = 0, 0
shark_size = 2
eat_cnt = 0
time = 0

dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i,j

graph[shark_x][shark_y]=0

def bfs(shark_x,shark_y):
    q = deque([(shark_x,shark_y,0)])
    dist_list = []
    visited = [[False]*n for _ in range(n)]
    visited[shark_x][shark_y] = True
    min_dist = int(1e9)
    
    while q:
        x,y,dist = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if graph[nx][ny] <= shark_size:
                    visited[nx][ny] = True
                    if 0<graph[nx][ny]<shark_size:
                        min_dist = dist
                        dist_list.append((dist+1,nx,ny)) # 이동 거리, 좌표
                    if dist+1 <= min_dist:
                        q.append((nx,ny,dist+1)) # 좌표, 이동거리 큐에 담는다

    if dist_list:
        dist_list.sort() # 
        return dist_list[0]
    else:
        return False

while fish_cnt:
    result = bfs(shark_x,shark_y)
    
    if not result: # 먹을 물고기가 없을 때
        break
    
    shark_x,shark_y = result[1],result[2] # 상어의 좌표
    time += result[0] # 이동거리
    eat_cnt += 1
    fish_cnt -= 1
    
    if shark_size == eat_cnt:
        shark_size += 1
        eat_cnt = 0
    
    graph[shark_x][shark_y] = 0

print(time)


    
                
        
            

        


