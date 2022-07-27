def solution(N, stages):
    peoples = len(stages)
    result = []
    ans = []
    
    for i in range(1, N+1):
        people = stages.count(i)
        if people == 0:
            result.append((0,i))
            continue
        fail_percent = people / peoples
        result.append((fail_percent, i))
        peoples -= people
    
    result.sort(key = lambda x : (-x[0],x[1]))
    
    for j in range(N):
        A, B = result[j]
        ans.append(B)
                
    return ans