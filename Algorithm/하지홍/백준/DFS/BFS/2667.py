from collections import deque

n = int(input())

direction = [[1,0],[-1,0],[0,-1],[0,1]]
graph = [list(map(int, input())) for _ in range(n)]
result = []

    
def bfs(graph, x, y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    cnt = 1
    
    
    while queue:
        x, y = queue.popleft()
        
        for next_move_x, next_move_y in direction:
            next_x = next_move_x + x
            next_y = next_move_y + y
            
            if next_x < 0 or next_x >=n or next_y < 0 or next_y >= n:
                continue
            
            if graph[next_x][next_y] == 1:
                graph[next_x][next_y] = 2
                queue.append((next_x,next_y))
                cnt += 1
                
    return cnt


result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(graph,i,j))
            
result.sort()

print(len(result))

for elem in result:
    print(elem)