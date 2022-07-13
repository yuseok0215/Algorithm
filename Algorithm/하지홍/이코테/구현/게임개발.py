N, M = map(int, input().split())

x, y, d = map(int, input().split())

game_map = []
for i in range(N):
    game_map.append(list(map(int, input().split())))
    
game_mark = [[0] * M for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]


game_mark[x][y] = 1
cnt = 1
dir_cnt = 0

while True:
    ## 왼쪽으로 방향 이동
    d -= 1
    if d < 0:
        d = 3
        
    next_x = x + dx[d]
    next_y = y + dy[d]
    
    if game_map[next_x][next_y] == 0 and game_mark[next_x][next_y] == 0:
        game_mark[next_x][next_x] == 1
        x, y = next_x, next_y
        cnt += 1
        dir_cnt = 0
        continue
    else:
        dir_cnt += 1
        
    if dir_cnt == 4:
        next_x = x - dx[d]
        next_y = y - dy[d]
        
        if game_map[next_x][next_y] == 0:
            x, y = next_x, next_y
        else:
            break
        dir_cnt = 0