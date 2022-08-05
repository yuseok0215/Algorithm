n, h = map(int, input().split())


down = [0] * n
up = [0] * n
for i in range(1,n+1):
    if i % 2 == 1:
        down[i] = int(input())
    else:
        up[i] = int(input())
        

result = []

    
for i in range(1, h):
    cnt = 0
    for elem in up:
        if elem < i:
            cnt += 1
    for elem in down:
        if h- elem < i:
            cnt += 1
    result.append(cnt)


min_result = min(result)

count = 0

for elem in result:
    if min_result == elem:
        count += 1
        
print(min_result, count)
    


    