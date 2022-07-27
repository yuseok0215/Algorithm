from collections import deque

n, k = map(int, input().split())

direction = [[1,0],[-1,0],[0,-1],[0,1]]

graph = []


for i in range(n):
    graph.append(list(map(int,input())))
    
s, x, y = map(int, input().split())

q = []

for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            q.append((graph[i][j],i,j))
            
queue = deque(sorted(q))


while s:
    temp_queue = deque()
    s-=1
    while queue:
        num,x,y = queue.popleft()
        for next_move_x,next_move_y in direction:
            now_x = x + next_move_x 
            now_y = y + next_move_y
            if 0 <= now_x < n and 0 <= now_y < n and graph[now_x][now_y] == 0:
                graph[now_x][now_y] = num
                temp_queue.append((num,now_x,now_y))
    if not temp_queue:
        break
    queue = temp_queue

print(graph[x-1][y-1])