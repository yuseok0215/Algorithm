import sys
import time
start_time=time.time()
sys.stdin=open("input.txt","rt")

n,k=map(int,input().split())
cnt=0
while n>1:
    if n%k==0:
        cnt+=1
        n=n//k
    else:
        n-=1
        cnt+=1
print(cnt)

end_time=time.time()
print("time: ", end_time-start_time)