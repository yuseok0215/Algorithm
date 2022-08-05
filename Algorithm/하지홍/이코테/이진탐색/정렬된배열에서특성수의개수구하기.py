n, x = map(int, input().split())

arr = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    
    if start > end:
        return 