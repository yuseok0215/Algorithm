T = int(input())
from collections import deque

for i in range(T):
    N, M = map(int, input().split())
    
    
    que = deque(list(map(int, input().split())))
    idx_que = deque(list(range(N)))
    cnt = 0
    
    while que:
        if que[0] == max(que):
            cnt += 1
            que.popleft()
            
            if idx_que.popleft() == M:
                print(cnt)
                break
        else:
            que.append(que.popleft())
            idx_que.append(idx_que.popleft())


    
    
    
    