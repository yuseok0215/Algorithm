import sys
import time
start_time=time.time()
sys.stdin=open("input.txt","rt")

n=int(input())
coins=list(map(int,input().split()))
check=[0]*sum(coins)

for i in range(n):
    for j in range(i,n):
            check[sum(coins[i:j+1])-1]=1
print(check)

print(check.index(0)+1)

end_time=time.time()
print("time: ", end_time-start_time)