data = input()
row = int(data[1])
column = int(ord(data[0]))-int(ord('a')) + 1


case = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

cnt = 0
for i in range(8):
    if row - case[i][0] > 0 and column - case[i][1] > 0:
        cnt += 1
    
print(cnt)
