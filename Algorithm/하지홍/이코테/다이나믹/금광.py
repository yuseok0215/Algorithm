t = int(input())

while t > 0:
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = []
    idx = 0
    for i in range(n):
        graph.append(arr[idx:idx+m])
        idx += m
    
    
    for i in range(1,m):
        for j in range(n):
            if j == 0:
                left_up = 0
            else:
                left_up = graph[j-1][i-1]
                
            if j == n-1:
                left_down = 0
            else:
                left_down = graph[j+1][i-1]
                
            left = graph[j][i-1]
            graph[j][i] = graph[j][i]+max(left_up, left_down, left)
            
    result = 0
    for i in range(n):
        result = max(result, graph[i][m-1])
    
    print(result)