import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
cnt = 0
answer = 0
arr = list(map(int, input().split()))
arr.sort(reverse=True)

if arr[0]!= arr[1]:
    for i in range(M):
        if cnt == K:
            answer += arr[1]
            cnt = 0
        else:
            answer += arr[0]
            cnt += 1
        
else:
    answer = arr[0]*M
    
print(answer)