T = int(input())


for i in range(0,T):
    
    appliers = []
    cnt = 1
    
    N = int(input())
    
    for i in range(N):
        test, interview = map(int, input().split())
        appliers.append([test, interview]) 
        
    appliers.sort(key = lambda x:x[0])
    
    max_appliers =appliers[0][1]
    
    for i in range(1,N):
        if max_appliers > appliers[i][1]:
            cnt += 1
            max_appliers = appliers[i][1]