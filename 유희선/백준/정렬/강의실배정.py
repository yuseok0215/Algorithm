import sys
sys.stdin=open("input.txt","rt")
input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
    s,e=map(int,input().split())
    arr.append((s,e))
arr.sort(key=lambda x: (x[1],x[0]))

cnt=0
visited=[0]*n
totalVisit=0
while totalVisit!=n:
    index=0
    endTime=-217000000
    for x in arr:
        if endTime<=x[0] and visited[index]==0:
            endTime=x[1]
            visited[index]=1
            totalVisit+=1
        index+=1
    cnt+=1
print(cnt)