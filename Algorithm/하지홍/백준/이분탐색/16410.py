m, n = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort(reverse=True)

left = 0
right = max(arr)
ans =0

while left <= right:
    cnt = 0
    
    mid = (left+right)//2
    
    #  예외처리
    if mid == 0:
        break
    
    for elem in arr:
        if elem >= mid:
            cnt += (elem//mid)
        else:
            break
    
    if cnt >= m:
        left = mid + 1
        ans = mid
    else:
        right = mid -1
        
print(ans)
        


