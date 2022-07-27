n = int(input())

arr = []

for i in range(n):
    arr += list(map(int, input().split()))
    arr = sorted(arr, reverse=True)[:n]

print(arr[-1])



## 다른 풀이
import heapq 

heap = []
n = int(input())

for _ in range(n):
    numbers = map(int, input().split())    
    for number in numbers:        
        if len(heap) < n: # heap의 크기를 n개로 유지            
            heapq.heappush(heap, number)        
        else:            
            if heap[0] < number:                
                heapq.heappop(heap)                
                heapq.heappush(heap, number)
print(heap[0])
