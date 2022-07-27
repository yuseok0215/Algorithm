n, l = map(int, input().split())

arr = []
for i in range(n):
    a,b = map(int, input().split())
    arr.append([a,b])

cnt = 0

position = 0

arr.sort(key= lambda x:x[0])

for start, end in arr:
    if position > start:
        start = position
    while start < end:
        start += l
        cnt += 1
    position = start
    
print(cnt)

