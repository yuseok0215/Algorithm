import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(N):
    for j in range(i+1,N):
        if arr[i] != arr[j]:
            cnt += 1
        
        
print(cnt)

