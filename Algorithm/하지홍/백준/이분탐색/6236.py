n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

left = min(arr)
right = sum(arr)

while left <= right:
    mid = (left+right) // 2
    
    cnt = 1
    
    now_money= mid
    
    
    for money in arr:
        if now_money-money < 0:
            cnt += 1
            now_money = mid
        now_money -= money
        
    if cnt > m or mid < max(arr):
        left = mid + 1
    else:
        right = mid - 1
        ans = mid

        
    
print(ans)