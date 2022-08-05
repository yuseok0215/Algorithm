n = int(input())

arr = list(map(int, input().split()))

arr.sort()

m = int(input())


arr_search =  list(map(int, input().split()))

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
    

for elem in arr_search:
    if binary_search(arr, elem, 0, len(arr)-1) == True:
        print(1)
    else:
        print(0)