n , m = map(int, input().split())

lecture = list(map(int, input().split()))

right = sum(lecture)
left = max(lecture)


while left <= right:
    mid = (left + right) // 2
    
    count = 0
    
    tmp = 0
    
    for i in range(n):
        if lecture[i] + tmp > mid:
            count += 1
            tmp = 0
        tmp += lecture[i]        
    
    if tmp:
        count += 1
    else:
        None
        

    if count <= m:
        right = mid-1
    else:
        left = mid + 1
        
print(left)

    
    
