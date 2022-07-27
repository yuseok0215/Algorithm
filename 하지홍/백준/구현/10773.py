K = int(input())

arr = []
cnt = 0

for i in range(K):
    num = int(input())
    
    if num == 0:
        del arr[-1]
    else:
        arr.append(num)
        
for elem in arr:
    cnt += elem

print(cnt)