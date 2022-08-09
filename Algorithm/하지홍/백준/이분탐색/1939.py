import sys
from collections import deque

def bfs(my_list, value, start, end, n):
    que = deque()
    v = [0 for _ in range(n+1)]
    
    v[start] = 1
    que.append(start)
    
    while que:
        asis = que.popleft()
        
        if asis == end:
            return True
        
        for togo, limit in my_list[asis]:
            if limit >= value and v[togo] == 0:
                que.append(togo)
                v[togo] = 1
                
    return False

n, m = map(int, input().split())
my_list = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    my_list[a].append((b,c))
    my_list[b].append((a,c))
    
s,e = map(int, input().split())
l, r = 0, sys.maxsize
answer = 0

while l <= r:
    mid = (l+r)//1
    if bfs(my_list, mid, s, e, n):
        l = mid+1
        answer = mid
    else:
        r = mid -1
        
print(answer)