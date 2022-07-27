## heapq 는 이진트리(Binary Tree)를 기반으로 한 최소 힙(min heap)정렬 트리
import heapq

n = int(input())

card = [int(input()) for _ in range(n)]

heapq.heapify(card)

result = 0

while len(card) > 1:
    a, b = heapq.heappop(card), heapq.heappop(card)
    result += a+b
    heapq.heappush(card, a+b)
    
print(result)
