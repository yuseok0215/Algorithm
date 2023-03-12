N = int(input())
M = int(input())
S = str(input())


I_cnt = N+1
O_cnt = N
cnt = 0
arr = []
for i in range(2*N+1):
    if i % 2 == 0:
        arr.append('I')
    else:
        arr.append('O')
        
tmp = "".join(arr)

for i in range(0,len(S)-(2*N)):
    if S[i:i+(2*N+1)] == tmp:
        cnt += 1
        
print(cnt)

N = int(input())
M = int(input())
S = input()
answer, i, count = 0, 0, 0

while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        i += 1
        count = 0

print(answer)
