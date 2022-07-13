import sys
import time
start_time=time.time()
sys.stdin=open("input.txt","rt")

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
maxNum=0
for i in range(n):
    minRow=min(arr[i])
    if maxNum<minRow:
        maxNum=minRow
print(maxNum)

end_time=time.time()
print("time: ", end_time-start_time)