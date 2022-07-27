N = int(input())


arr = []
for i in range(N):
    arr.append(int(input()))
    
arr.sort(reverse=True)


for i in range(N):
    arr[i] = arr[i] * (i+1)
    
print(max(arr))