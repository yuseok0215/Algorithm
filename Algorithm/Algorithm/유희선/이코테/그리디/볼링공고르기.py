import sys
sys.stdin=open("input.txt","rt")

n,m=map(int,input().split())
heights=list(map(int,input().split()))
cnt=0

for i in range(n):
    for j in range(i+1,n):
        if heights[i]==heights[j]:
            continue
        cnt+=1
print(cnt)