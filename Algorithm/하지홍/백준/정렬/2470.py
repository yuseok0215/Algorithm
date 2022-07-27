n = int(input())

## 산성용액(1~1,000,000,000), 알칼리성 용액(-1, -1000000000)
from itertools import combinations
standard = 1e9

arr = list(map(int, input().split()))
result = []
combin = list(combinations(arr, r =2))

for elem in combin:
    result.append(sum(elem))

for elem in result:
    length = abs(elem)
    if standard > length:
        standard = length
        
answer = 0

for elem in combin:
    if abs(sum(elem)) == standard:
        answer = elem
        break

ab = sorted(list(answer))

for elem in ab:
    print(elem, end=' ')
    
    
    
