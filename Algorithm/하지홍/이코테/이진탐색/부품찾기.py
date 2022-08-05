

n  = int(input())
now_arr = list(map(int, input().split()))
m = int(input())
require_arr = list(map(int, input().split()))

now_arr.sort()

def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start+end)//2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
for elem in require_arr:
    if binary_search(now_arr,elem,0, n-1) == True:
        print('yes', end= ' ')
    else:
        print('no', end=' ')