n, m = map(int, input().split())

arr = list(map(int, input().split()))

def binary_search(array, target, start, end):
    
    ans = 0
    
    while start <= end:
        mid = (start+end)//2
        total = 0
        
        for i in array:
            if i > mid:
                total += i -mid
            
        if total < target:
            end = mid - 1
            
        else:
            start = mid+1
            ans = mid
    return ans
    
print(binary_search(arr, m, 0, max(arr)))