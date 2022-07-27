import heapq

n = int(input())

heap = []

for _ in range(n):
    arr = list(map(int, input().split())) # n = 5 / 10 2 3 4 5
    if not heap:
        for a in arr:
            heapq.heappush(heap, a) # 오름차순 정렬
    else:
        for a in arr:
            if heap[0] < a:
                heapq.heappush(heap, a)
                heapq.heappop(heap)

print(heap[0])

