N = int(input())

cnt = 0

time_list = []
for i in range(N):
    start_time, end_time = map(int, input().split())
    time_list.append([start_time, end_time])
    
time_list.sort(key= lambda x:(x[1],x[0]))



limit = 0
for start, end in time_list:
    if start >= limit:
        cnt +=1
        limit = end

print(cnt)