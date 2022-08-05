n, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()

start = 1
end = arr[-1]-arr[0]
result = 0


while start <= end:
    mid = (start+end)//2
    value = arr[0]