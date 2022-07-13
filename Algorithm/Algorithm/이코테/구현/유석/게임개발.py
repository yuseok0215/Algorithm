n, m = map(int, input().split())
x, y, direction = map(int, input().split())

d = [[0] * m for _ in range(n)]
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
d[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 -1]

def turn_left(): # 방향에 대한 인덱스 연산
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt =  1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0


print(cnt)




