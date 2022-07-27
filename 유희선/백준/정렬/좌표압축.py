import sys
sys.stdin=open("input.txt","rt")
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
res=[]
for now in arr:
    cnt=0
    prev=[]
    for x in arr:
#2 4 -10 4 -9
        if now>x and x not in prev:
            cnt+=1
            prev.append(x)
    res.append(cnt)

for x in res:
    print(x, end=' ')