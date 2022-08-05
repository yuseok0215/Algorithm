n, k = map(int, input().split())

arr = []

for i in range(n):
    arr.append(str(i+1))
    
result = ''.join(arr)

start = 0
end = len(result)

def binary_search(array, target, left, right):
    mid = (left+right)//2
    
    if mid == target:
        print(result[mid-1])
    elif mid > target:
        binary_search(array, target, left, mid-1)
    else:
        binary_search(array, target, mid+1, right)
        


print(binary_search(result, k, start, end))

## 다른 풀이
n, k = map(int, input().split())
ans = 0
digit = 1
nine = 9

while k > digit*nine:
    k = k-(digit * nine)
    ans = ans + nine
    digit+=1
    nine = nine*10

ans = (ans+1) + (k-1) // digit

if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1)%digit])