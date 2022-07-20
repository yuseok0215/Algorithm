import sys
sys.stdin=open("input.txt","rt")
from collections import deque
n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))
q=deque()
x,y=0,0
q.append((x,y))
graph[x][y]=0
goal_x,goal_y=n-1,m-1
dx=[-1,1,0,0]
dy=[0,0,-1,1]
cnt=0
while x!=goal_x or x!=goal_y:
    x,y=q.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if graph[nx][ny]==0:
            continue
        if graph[nx][ny]==1:
            cnt+=1
            q.append(nx,ny)
            graph[nx][ny]=0