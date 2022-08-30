n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i
    
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i+1, j+1)
            
trip = list(map(int, input().split()))

temp = True

for i in range(m-1):
    if find_parent(parent, trip[i]) != find_parent(parent, trip[i+1]):
        temp = False
        
if temp == True:
    print("YES")
else:
    print("NO") 
        