import sys
from itertools import combinations
input = sys.stdin.readline

arr = sorted(list(map(int, input().split())))


new_arr = []
new_result = []
for i in range(1,len(arr)+1):
    new_arrs = list(combinations(arr,i))
    for elem in new_arrs:
        new_result.append(sum(elem))
    
new_results = sorted(list(set(new_result)))
print(new_results)

cnt = 1

for i in range(len(new_results)):
    if new_results[i] == cnt:
        cnt += 1
    else:
        break
        
print(cnt)

#### 
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# target = 1
# for x in data:
#     if target < x:
#         break
#     target += x
# print(target)