from collections import deque

n, m = map(int, input().split()) # 세로, 가로 입력

map = []
temp = [[0]*m for _ in range(n)] # 벽 3개를 설치한 뒤 임시 맵
for _ in range(n):
    map.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
# 벽을 임의로 3개를 세우고, 바이러스를 퍼트린 뒤, 남은 생존 영역을 체킹해서 배열에 담고 제일 큰 수를 출력하자

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny) # 바이러스 퍼트리기

def safety_map():
    s_map_cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                s_map_cnt += 1

    return s_map_cnt

def dfs(count):
    
    global result
    # 벽이 총 3개인 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = map[i][j]
        # 바이러스 퍼트리기
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, safety_map())
        return
    
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                map[i][j] = 1
                count += 1

                dfs(count)
                map[i][j] = 0
                count -= 1

    
dfs(0)
print(result)


        

        