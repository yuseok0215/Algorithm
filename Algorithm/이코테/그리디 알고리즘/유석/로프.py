import sys

n = int(input())

data = []
result = []
for i in range(n):
    data.append(int(input()))

data.sort()
for l in range(n):
    result.append(data[l] * (n-l))

print(max(result))
