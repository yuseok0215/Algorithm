k = int(input())

data = []
for i in range(k):
    inp = int(input())
    if inp == 0:
        data.pop()
    else:
        data.append(inp)

result = 0
for i in data:
    result += i

print(result)