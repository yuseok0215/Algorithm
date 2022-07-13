import sys
n=int(input())
meeting=[]
for i in range(n):
    s,e=map(int,sys.stdin.readline().split())
    meeting.append((s,e))
meeting.sort(key=lambda x:(x[1],x[0]))
end=0
cnt=0
for s,e in meeting:
    if end<=s:
        end=e
        cnt+=1
print(cnt)