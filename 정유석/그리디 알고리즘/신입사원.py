import sys
t = int(input())

test = []
for i in range(t):
    cnt = 1
    people = []
    
    n = int(input())
    for i in range(n):
        paper, interview = map(int,sys.stdin.readline().split())
        test.append([paper, interview])

    test.sort()
    
    max = test[0][1]

    for l in range(1, n):
        if max > test[i][1]:
            cnt += 1
            max = test[i][1]
    print(cnt)

