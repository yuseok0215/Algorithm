import sys
import time
start_time=time.time()

sys.stdin=open("input.txt","rt")
n,m,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
mCnt=0
kCnt=0
sum=0
while mCnt!=m:
    sum+=arr[0]
    mCnt+=1
    kCnt+=1
    if kCnt==k:
        kCnt=0
        sum+=arr[1]
        mCnt+=1
print(sum)

end_time=time.time()
print("time: ", end_time-start_time)