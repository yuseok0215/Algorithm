n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()


result = 0
index = 0
for i in range(len(A)):
    max = 0
    for k in range(len(B)):
        if max < B[k]:
            max = B[k]
            index = k
    B[index] = -1
    result += A[i]*max

print(result)