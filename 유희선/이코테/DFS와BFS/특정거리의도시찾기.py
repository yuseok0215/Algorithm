import sys
sys.stdin=open("input.txt","rt")
from collections import deque

n,m,k,x=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1 #정점간의 연결정보 저장

def bfs(start,minDis):
    q=deque()
    q.append(start)
    visited=[False]*(n+1) #방문여부
    visited[start]=True
    dis=[-1]*(n+1) #거리저장
    dis[start]=0
    res=[]
    while q:
        x=q.popleft()
        for v in range(1,n+1):
            if graph[x][v]==1 and not visited[v]:
                visited[v]=True
                dis[v]=dis[x]+1
                if dis[v]==minDis:
                    res.append(v)
                q.append(v)
    return res

res=bfs(x,k)
if res:
    res.sort()
    for x in res:
        print(x)
else:
    print(-1)