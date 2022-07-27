n = int(input())

time = []
for _ in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time, key=lambda a: a[0]) # 시작시간을 기준으로 오름차순 정렬
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 오름차순 정렬

last = 0
cnt = 0

for i,j in time:
    if i>= last:
        cnt += 1
        last = j

print(cnt)