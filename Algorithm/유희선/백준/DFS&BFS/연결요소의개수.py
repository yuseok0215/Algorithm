import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
data=[[0]*n for _ in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    data[u-1][v-1]=1
    data[v-1][u-1]=1
visited=[False]*n
cnt=0

def bfs(start,visit,cnt):
    q=deque()
    q.append(start)
    while q:
        v=q.popleft()
        for i in range(n):
            if data[v][i]==1 and not visited[i]:
                visited[i]=True
                q.append(i)
    cnt+=1
    return (visited,cnt)

visited,cnt=bfs(1,visited,cnt)

while False in visited:
    v=visited.index(False)
    visited,cnt=bfs(v,visited,cnt)

print(cnt)