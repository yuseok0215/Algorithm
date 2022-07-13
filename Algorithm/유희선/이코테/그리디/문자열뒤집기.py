import sys
import time
start_time=time.time()
sys.stdin=open("input.txt","rt")

s=input()
cnt0=cnt1=0
before=s[0]

for i in range(1,len(s)):
    if s[i]!=before:
        if before=='0':
            cnt0+=1
        else:
            cnt1+=1
        before=s[i]

#마지막 그룹체크
if s[-1]=='0':
    cnt0+=1
else:
    cnt1+=1

if cnt0>=cnt1:
    print(cnt1)
else:
    print(cnt0)

end_time=time.time()
print("time: ", end_time-start_time)