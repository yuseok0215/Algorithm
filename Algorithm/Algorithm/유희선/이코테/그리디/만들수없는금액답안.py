import sys
import time
start_time=time.time()
sys.stdin=open("input.txt","rt")

n=int(input())
coins=list(map(int,input().split()))
coins.sort()
target=1

for x in coins:
    if target<x:
        break
    target+=x
print(target)

end_time=time.time()
print("time: ", end_time-start_time)