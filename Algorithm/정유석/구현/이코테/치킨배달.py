from itertools import combinations

n, m = map(int, input().split())
chicken, city = [], []

for i in range(n):
    data = list(map(int, input().split()))
    for l in range(n):
        if data[l] == 1:
           city.append((i, l))
        elif data[l] == 2:
            chicken.append((i,l))

c_list = list(combinations(chicken, m))

def get_sum(c_list):
    result = 0

    for cx, cy in city:
        temp = 1e9
        for dx, dy in c_list:
            temp = min(temp, abs(cx - dx) + abs(cy- dy))
        result += temp

    return result

result = 1e9
for c in c_list:
    result = min(result, get_sum(c))      

print(result)
 
