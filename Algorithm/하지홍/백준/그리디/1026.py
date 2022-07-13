N = int(input())

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

arr_A.sort(reverse=False)
arr_B.sort(reverse=True)


cnt = 0 

for i in range(N):
    cnt += arr_A[i] * arr_B[i]
    
print(cnt)
