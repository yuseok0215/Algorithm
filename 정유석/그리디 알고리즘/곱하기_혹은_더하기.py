
S = input()

if int(S[0]) != 0:
    result = int(S[0])
    for i in range(1, len(S)):
        if S[i] == '0':
            result += int(S[i])
        else:
            result *= int(S[i])    
else:
    result = 1
    for i in range(1, len(S)):
        if S[i] == '0':
            result += int(S[i])
        else:
            result *= int(S[i])

print(result)
