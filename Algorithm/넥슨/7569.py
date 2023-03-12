from collections import deque

m , n  = map(int, input().split())
cnt = 0
direction = [[1,0],[-1,0],[0,-1],[0,1]]
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    cnt += graph[i].count(0)
    
if cnt == 0:
    print(0)
    exit()
    
def bfs():
    while queue:
        x, y = queue.popleft()
        for next_move_x, next_move_y in direction:
            dx = next_move_x + x
            dy = next_move_y + y
            
            if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 0:
                graph[dx][dy] = graph[x][y] + 1
                queue.append([dx, dy])
                
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i,j])
        
bfs()

cnt_0 = 0

for i in graph:
    cnt_0 += i.count(0)
    
    if cnt_0 > 0:
        print(-1)
        exit()
        
    
day_cnt = 0
for elem in graph:
    day_cnt = max(day_cnt, max(elem))

print(day_cnt - 1)