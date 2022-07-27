n, L_len = map(int, input().split())

sand_graph = []
for _ in range(n):
    sand_graph.append(list(map(int, input().split())))

sand_graph = sorted(sand_graph, key=lambda x:x[0])


index = 0
L_count = 0
L_pointer = sand_graph[0][0]
while index<n:
    W_start = sand_graph[index][0]
    W_finish = sand_graph[index][1]
    
    if L_pointer <= W_start:
        L_pointer = W_start

    if L_pointer < W_finish:  
        L_pointer += L_len
        L_count += 1
    else: # 널빤지로 물 웅덩이를 다 가렸을 때
        index += 1


print(L_count)
        
    
    
