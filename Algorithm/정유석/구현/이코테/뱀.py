n = int(input())
board = [[0]*(n) for _ in range(n)]

k = int(input())
for i in range(k):
    m,n = map(int, input().split())
    board[m-1][n-1] = 1 # 사과 위치 1로 표시

d = int(input())
info = []
for i in range(d):
    x, c = input().split()
    info.append((int(x), c))

time = 0
direction = 0 # 현재 위치 동방향
dx = [0, 1, 0, -1] # 동 남 서 북
dy = [1, 0, -1, 0]
x, y = 1, 1
board[x][y] = 2 # 시작시점의 뱀 위치 2로 표시
snack = [(x,y)]
rotate_index = 0 # 회전 정보 인덱스
while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2: # 맵 범위 내에 있으며, 뱀 몸통이 없는 위치라면
        if board[nx][ny] == 0: # 사과가 없다면
            board[nx][ny] = 2
            snack.append((nx, ny))
            px, py = snack.pop(0) # 원래 뱀이 있었던 위치
            board[px][py] = 0 # 초기화
        else: # 사과가 있다면
            board[nx][ny] = 2
            snack.append((nx, ny))
    else: # 벽이나 뱀의 몸통과 부딫혔다면
        time += 1
        break
    
    x, y = nx, ny # 다음 위치로 머리 이동
    time += 1

    if rotate_index < d and info[rotate_index][0] == time: # 첫번째 조건문 질문
        if info[rotate_index][1] == "L":
            direction = (direction-1) % 4 # %4: out of range 방지
        else:
            direction = (direction+1) % 4
        rotate_index += 1

print(time)