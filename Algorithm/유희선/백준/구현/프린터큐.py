import sys
from collections import deque
input=sys.stdin.readline

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    arr=deque(map(int,input().split()))
    index=deque(range(n))
    cnt=0
    while arr:
        if arr[0]==max(arr):
            cnt+=1
            arr.popleft()
            i=index.popleft()
            if i==m:
                print(cnt)
                break
        else:
            arr.append(arr.popleft())
            index.append(index.popleft())