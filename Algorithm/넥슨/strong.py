import heapq
from collections import deque
def getMinimumHealth(initial_players, new_players, rank):
    # Write your code here
    initial_players
    heapq.heapify(initial_players)
    queue = deque(new_players)
    cnt = 0
    cnt += initial_players[-rank] 
    while queue:
        value = queue.popleft()
        heapq.heappush(initial_players, value)
        cnt += initial_players[-rank]
        
    return cnt


getMinimumHealth([1,3,2],[6,4,5],3)
