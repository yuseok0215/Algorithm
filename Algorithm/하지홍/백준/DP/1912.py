n = int(input())

arr_list = list(map(int,input().split()))

for i in range(1, len(arr_list)):
    if arr_list[i-1] > 0:
        arr_list[i] += arr_list[i-1]
    else:
        continue


print(max(arr_list))

