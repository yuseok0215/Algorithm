t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    
    if point[x][y] == 1:
        point[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

        return True
    
    return False

result = []
for m in range(t):
    m, n, k = map(int, input().split())

    point = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        point[b][a] = 1
        
    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                count += 1
    result.append(count)

for i in range(len(result)):
    print(result[i])