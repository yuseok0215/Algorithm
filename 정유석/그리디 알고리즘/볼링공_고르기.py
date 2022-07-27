from itertools import combinations

m, n = map(int, input().split())

data = list(map(int, input().split()))

c_data = list(combinations(data, 2))
print(c_data)
cnt = 0
for i in range(len(c_data)):
    if c_data[i][0] == c_data[i][1]:
        cnt += 1

print(len(c_data)-cnt)

