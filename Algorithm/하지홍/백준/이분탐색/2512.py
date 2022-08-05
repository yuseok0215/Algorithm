
n = int(input())
arr = list(map(int, input().split()))
money = int(input())

left_side = 0
right_side = max(arr)

while left_side <= right_side:
    mid = (left_side+right_side) // 2
    
    result = 0
    
    for x in arr:
        if mid >= x:
            result += x
        else:
            result += mid
            
    if result <= money:
        left_side = mid + 1
    else:
        right_side = mid -1
        
print(right_side)
