import sys
#sys.stdin=open("input.txt","rt")
input=sys.stdin.readline
k=int(input())
stack=[]
for i in range(k):
    x=int(input())
    if x==0:
        stack.pop()
    else:
        stack.append(x)
print(sum(stack))