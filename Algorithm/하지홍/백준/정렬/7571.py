n , m = map(int, input().split())

# graph = [[0]*n for _ in range(n)]

x_list = []
y_list = []

for i in range(m):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
    
    
x_list.sort()
y_list.sort()

position_x = x_list[m//2]
position_y = y_list[m//2]

sum = 0


for i in range(m):
    sum += abs(x_list[i]-position_x) + abs(y_list[i]-position_y)
    
print(sum)
