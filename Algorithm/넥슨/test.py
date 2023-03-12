def check(target, source):
    answer = 0
    dp=[[0] * (len(source) + 1) for _ in range(len(target) + 1)]

    for i in range(1, len(target)+1):
        for j in range(1, len(source)+1):
            if (target[i-1] == source[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
                answer = max(dp[i][j], answer)
                
    if answer == len(target):
        return True
    else:
        False
        
def getMaximumRemovals(order, source, target):
    # Write your code here
    cnt = 0
    if source == target:
        return cnt
    
    for idx in order:
        listResult = list(source)
        listResult[idx-1] = ""
        source = "".join(listResult)
        cnt += 1
        if check(target,source) == True:
            continue
        else:
            break
    return cnt


                
        
        
        
        
print(getMaximumRemovals([1, 4, 2, 3, 5],"hkbdi","kd"))