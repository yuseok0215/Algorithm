t = int(input())
from collections import deque


for _ in range(t):
    n = int(input())
    queue = deque()
    arr = sorted(list(map(int, input().split())), reverse=True)
    max_num = -1e9
    
    for i in range(len(arr)):
        if i % 2 == 0:
            queue.append(arr[i])
        else:
            queue.appendleft(arr[i])
            

    for i in range(len(queue)-1):
        nums = abs(queue[i]-queue[i+1])
        if nums > max_num:
            max_num = nums
            
    print(max_num)
        
            
    