n = int(input())
data = list(map(int, input().split()))

data.sort()

num = 1
for i in data:
    if num < i:
        break

    num += i

print(num)    


    

