def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m: #index는 0~n-1 또는 0~m-1
        return False
    
    if ice_cream[x][y] == 0:
        ice_cream[x][y] = 1

        dfs(x, y+1) 
        dfs(x, y-1) 
        dfs(x-1, y) 
        dfs(x+1, y) 
        return True
    
    return False

n, m = map(int, input().split())

ice_cream = []
for i in range(n):
    ice_cream.append(list(map(int, input())))

ice_cnt = 0
for i in range(n):
    for l in range(m):
        if dfs(i, l) == True:
            ice_cnt += 1

print(ice_cnt)
    
