import sys
sys.stdin=open("input.txt","rt")
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
plus=[]
minus=[]
for x in arr:
    if x<0:
        minus.append(x)
    else:
        plus.append(x)
pl=len(plus)
minDis=1e9
for i in range(len(minus)):
    for j in range(pl):
        dis=abs(minus[i]+plus[j])
        if dis<minDis:
            minDis=dis
            res=(minus[i],plus[j])
print(res[0],res[1])