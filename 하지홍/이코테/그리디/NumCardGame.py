import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(N)]

max_number = 0


for i in range(N):
    if max_number < min(arr[i]):
        max_number = min(arr[i])
        
print(max_number)

