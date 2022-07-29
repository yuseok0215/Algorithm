import heapq

n = int(input())

arr = []
classes = []

for i in range(n):
    a,b = map(int, input().split())
    arr.append((a,b))
    
arr.sort(key=lambda x : x[0])
# print(arr)

heapq.heappush(classes, arr[0][1])

for i in range(1, n):
    a, b = arr[i][0], arr[i][1]
    if a >= classes[0]:
        heapq.heappop(classes)
        heapq.heappush(classes,b)
    else:
        heapq.heappush(classes, b)
        
print(len(classes))
        

        

