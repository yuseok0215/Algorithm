N, K = map(int, input().split());

arr = []
cnt = 0

for i in range(N):
    arr.append(int(input()))
    
arr.sort(reverse=True)

for elem in arr:
    if K == 0:
        break
    if elem > K:
        continue
    cnt += K // elem
    K %= elem
    
    
print(cnt)
        