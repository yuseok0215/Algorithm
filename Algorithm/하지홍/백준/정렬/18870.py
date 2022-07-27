n = int(input())

arr = list(map(int, input().split()))

next_arr = list(sorted(set(arr)))

#### {999, 1000}
dic = {value: index for index, value in enumerate(next_arr)}

for elem in arr:
    print(dic[elem], end=' ')