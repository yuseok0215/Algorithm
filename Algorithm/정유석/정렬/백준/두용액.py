from sympy import Sum


n = int(input())
arr = sorted(list(map(int, input().split())))

start = 0
end = len(arr)-1

min = 1e9
while start < end:
    Sum = arr[start] + arr[end]  # -2 4 -99 -1 98 -> -99 -2 -1 4 98
    if abs(Sum) < min:
        min = abs(Sum)
        answer = arr[start], arr[end]
    if Sum == 0:
        break
    if Sum < 0:   
        start += 1
    else:
        end -= 1

for i in sorted(answer):
    print(i, end=' ')

