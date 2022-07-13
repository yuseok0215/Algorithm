from asyncio.constants import ACCEPT_RETRY_DELAY
import sys
import time
start_time=time.time()
sys.stdin=open("input.txt","rt")

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
group=0
cnt=0
for x in arr:
    group+=1
    if group==x:
        group=0
        cnt+=1
print(cnt)

end_time=time.time()
print("time: ", end_time-start_time)