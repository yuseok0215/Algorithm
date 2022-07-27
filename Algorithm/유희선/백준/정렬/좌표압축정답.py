import sys
sys.stdin=open("input.txt","rt")
n = int(input())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

numset = set(numbers)
a = list(numset)
a.sort()

numdict = {}
for i in range(len(a)):
    numdict[a[i]] = i
print(numdict)
for i in numbers:
    print(numdict[i], end=' ')