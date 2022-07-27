import sys
sys.stdin=open("input.txt","rt")
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    arr[i].sort(reverse=True)

for x in arr:
    print(x)

for i in range(n-1):
    for j in range(n):
        if arr[i][j]>arr[n-1][-1]:
            arr[n-1].pop()
            arr[n-1].append(arr[i][j])
            arr[n-1].sort(reverse=True)
        else:
            break
       
print(arr[n-1][-1])