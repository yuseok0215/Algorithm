def solution(food_times, k):
    cnt0=0
    time=0
    i=0
    l=len(food_times)
    while time<k:
        if food_times[i]==0:
            i+=1
            cnt0+=1
            if cnt0==l:
                break
        else:
            food_times[i]-=1
            time+=1
            i+=1
        i=i%l
    if cnt0==l:
        answer=-1
    else:
        answer = i+1
    return answer