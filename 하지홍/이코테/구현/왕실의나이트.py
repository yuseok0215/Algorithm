data = input()
column = int(ord(data[0]))-int(ord('a')) + 1
row = int(data[1])
cnt = 0

moves = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]


for move in moves:
    dx = row + move[0]
    dy = column + move[1]
    
    if dx >=1 and dx <= 8 and dy >=1 and dy <= 8:
        cnt += 1
        
print(cnt)
