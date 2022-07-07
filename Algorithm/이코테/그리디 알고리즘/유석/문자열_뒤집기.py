S = input()

S_length = len(S) 
cnt_zero = 0
cnt_one = 0
n = S[0]
for i in range(1, S_length):
    if n == S[i]:
        continue
    else:
        n = S[i]
        if n == '0':
            cnt_one += 1
        else:
            cnt_zero += 1

if S[S_length-1] == '0':
    cnt_zero += 1
else:
    cnt_one += 1

print(min(cnt_zero, cnt_one))