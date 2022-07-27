import collections

t = int(input())

answer = []
for _ in range(t):
    arr = []
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    
    queue = collections.deque()
    for i in range(n):
        if i%2 != 0: # 홀수일때
            queue.appendleft(arr[i])
        else:
            queue.append(arr[i])

    #queue = list(queue)
    
    #min = abs(queue[n-1] - queue[0])
    for i in range(n-1): # 차이의 최솟값
        queue = abs(arr[i] - arr[i+1])
        if queue < min:
            min = queue

    answer.append(min)

for elem in answer:
    print(elem)

