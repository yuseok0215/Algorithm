import sys
sys.stdin=open("input.txt","rt")
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    res=[]
    check=[0]*n
    for i in range(0,n,2):
        res.append(arr[i])
        check[i]=1
    for i in range(n-1,-1,-1):
        if check[i]==0:
            res.append(arr[i])
    maxDis=-217000000
    for i in range(0,n):
        dis=res[i]-res[i-1]
        if dis>maxDis:
            maxDis=dis
    print(maxDis)