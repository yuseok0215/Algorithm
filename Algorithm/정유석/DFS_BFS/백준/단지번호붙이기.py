from collections import deque # 백준 틀림

n = int(input())

cnt = 0
house_cnt = []
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))
    
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] != 0:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
                    cnt += 1
    

for i in range(n):
    for j in range(n):
        cnt = 1
        bfs(i,j)
        if cnt != 0:
            house_cnt.append(cnt)

house_cnt.sort()
print(len(house_cnt))
for i in range(len(house_cnt)):
    print(house_cnt[i])
                
