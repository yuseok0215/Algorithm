import sys
sum=0
x=0
n=0
s=int(input())
while sum<s:
    x+=1
    sum+=x
    n+=1
if sum==s:
    print(n)
else:
    print(n-1)