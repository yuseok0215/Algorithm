def check(u):
    arr= []
    for elem in u:
        if elem == '(':
            arr.append(elem)
        else:
            if not arr:
                return False
            arr.pop()
    return True


def solution(p):
    answer = ''
    if not p:
        return ''
    
    close_cnt = 0
    open_cnt = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            open_cnt += 1
        else:
            close_cnt += 1
            
        if open_cnt == close_cnt:
            u = p[:i+1]
            v = p[i+1:]
            break
    if check(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        for elem in u[1:-1]:
            if elem == ')':
                answer += '('
            else:
                answer += ')'
    return answer
        


