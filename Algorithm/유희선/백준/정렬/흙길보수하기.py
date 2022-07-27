import sys
sys.stdin=open("input.txt","rt")

n,l=map(int,input().split())
water=[]
check=[0]*1000000000
for _ in range(n):
    s,e=map(int,input().split())
    water.append((s,e))

water.sort()
max_water=water[-1][1]

for s,e in water:
    for i in range(s,e):
        check[i]=1
cnt=0
for i in range(1,max_water+1):
    if check[i]==1:
        for j in range(i,i+l):
            check[j]=2
        i=i+l
        cnt+=1
print(cnt)