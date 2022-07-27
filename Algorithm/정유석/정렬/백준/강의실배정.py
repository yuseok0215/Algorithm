from collections import deque

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key = lambda x:x[1])

queue = deque()
for i in range(n):
    queue.append(arr[i])

room = 1
index = 1
finish_time = 0
while queue:
    x, y = queue.popleft()
    finish_time += y

    for i in range(len(queue)):
        nx, ny = queue.pop(i)
        if y == queue[i][0]:
            finish_time += ny
        else:
            if nx < finish_time:
                room += 1

             
print(room)



    