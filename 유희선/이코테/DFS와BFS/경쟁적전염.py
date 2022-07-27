import sys
sys.stdin=open("input.txt","rt")
from collections import deque
n,k=map(int,input().split())
graph=[] #전체 보드 정보
data=[] #바이러스 정보
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j]!=0:
            data.append((graph[i][j],0,i,j)) #바이러스가 존재하면 (바이러스 종류, 시간, 위치 x, y) 삽입
data.sort() #낮은 번호의 바이러스가 먼저 증식하므로 바이러스 번호 순으로 정렬
q=deque(data)
target_s,target_x,target_y=map(int,input().split())

dx=[-1,0,1,0] #바이러스 퍼져나갈 수 있는 위치
dy=[0,1,0,-1]

while q:
    virus,s,x,y=q.popleft()
    if s==target_s:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny]==0: #아직 방문하지 않은 위치이므로 바이러스 전파하기
                graph[nx][ny]=virus
                q.append((virus,s+1,nx,ny))
print(graph[target_x-1][target_y-1])