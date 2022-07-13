import sys
import time
start_time=time.time()
sys.stdin=open("input.txt","rt")

s=input()
res=int(s[0])
for i in range(1,len(s)):
    if res==0 or res==1 or s[i]=='0' or s[i]=='1':
        res+=int(s[i])
    else:
        res*=int(s[i])
print(res)

end_time=time.time()
print("time: ", end_time-start_time)