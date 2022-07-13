import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

# 오름차순으로 정리
arr.sort()

group = 0
result = 0

for horror in arr:
    group += 1
    
    if horror <= group:
        result += 1
        group = 0
        



print(result)