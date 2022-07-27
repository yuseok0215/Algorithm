n = int(input())

dic = {}
arr = list(map(int, input().split()))

s_arr = sorted(set(arr))

for i in range(len(s_arr)):
    dic[s_arr[i]] = i

for j in arr:
    print(dic[j], end=' ')