def solution(s): 

    answer = len(s)
    
    if len(s) == 1:
        return 1
        
    for i in range(1, (len(s)//2) + 1):
        slice = s[0:i]
        cnt = 1
        result = ''
            
        for j in range(i, len(s), i):
            if slice == s[j:j+i]:
                cnt += 1
            else:
                    ## 값이 다른게 나와서 압축해야할때
                if cnt == 1:
                    result += slice
                    ## 압축이 가능할때
                else:
                    result += str(cnt) + slice
                cnt = 1
                slice = s[j:j+i]
            
        if cnt == 1:
            result += slice
        else:
            result += str(cnt) + slice
            
        answer = min(answer, len(result))
