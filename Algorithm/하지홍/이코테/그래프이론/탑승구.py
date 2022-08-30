def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, x)
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
g = int(input())
p = int(input())

parent = [0] * (g+1)

for i in range(1, g+1):
    parent[i] = i
    
cnt = 0

for i in range(p):
    nums = int(input())
    result = find_parent(parent, nums)
    
    if result == 0:
        break
    union_parent(parent, nums, nums-1)
    cnt += 1
    
    
print(cnt)
