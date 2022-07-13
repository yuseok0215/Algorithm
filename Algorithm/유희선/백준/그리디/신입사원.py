import sys
sys.stdin=open("input.txt","rt")
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    score=[]
    s2Min=2147000000
    cnt=0
    for i in range(n):
        s1,s2=map(int,input().split())
        score.append((s1,s2))
    score.sort()
    for x in score:
        if x[1]<s2Min:
            s2Min=x[1]
            cnt+=1
    print(cnt)