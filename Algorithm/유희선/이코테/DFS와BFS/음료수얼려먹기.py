import sys
sys.stdin=open("input.txt","rt")
import time
start_time=time.time()

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if -1<x<n and -1<y<m:
        if graph[x][y]==0:
            graph[x][y]=1
            dfs(x-1,y)#상
            dfs(x,y-1)#좌
            dfs(x+1,y)#하
            dfs(x,y+1)#우
            return True
    return False #graph[x][y]값이 1인 경우

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)
end_time=time.time()
print("time: ", end_time-start_time)