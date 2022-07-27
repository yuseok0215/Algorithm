def self_number(i):
    i = i + sum(map(int, str(i)))
    return i

arr = [0] * 10001   

for i in range(1, 10001):
    arr[i] = self_number(i)
    
for i in range(1,10001):
    if i not in arr:
        print(i)