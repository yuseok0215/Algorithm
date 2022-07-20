from collections import deque

n, m = map(int, input().split())

direction = [[1,0],[-1,0],[0,-1],[0,1]]

graph = []

for i in range(n):
    graph.append(list(map(int, input())))
    
    
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1
    
    while queue:
        present_x, present_y = queue.popleft()
        
        for next_move_x, next_move_y in direction:
            next_x = present_x + next_move_x
            next_y = present_y + next_move_y
            
            if 0 <= next_x < n and 0 <= next_y < m:
                if graph[next_x][next_y] == 0:
                    queue.append((next_x, next_y))
                    graph[next_x][next_y] = 1

cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i,j)
            cnt += 1

print(cnt)  
            
