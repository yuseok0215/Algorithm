import sys
sys.stdin=open("input.txt","rt")

n,m=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
temp=[[0]*m for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
reuslt=0

def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)

def get_score():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score

def dfs(count):
    global result
    #울타리 3개 설치된 경우, 그 결과를 temp배열에 저장. 
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=data[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        #안전영역 최댓값계산
        result=max(result,get_score())
        return
    #빈공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                count+=1
                dfs(count) #??
                data[i][j]=0 #??
                count-=1 #??

dfs(0)
print(result)