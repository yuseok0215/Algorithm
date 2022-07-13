k = int(input())

food_times = list(map(int, input().split()))

i=0
k_cnt = 0
while k_cnt < k:
    if food_times[i] != 0:
        food_times[i] -= 1

    i += 1    

    if i == len(food_times):
        i = 0

    k_cnt += 1
        
for k in range(len(food_times)):
    m = k+i
    if m == len(food_times):
        k = 0
        i = 0
    if food_times[m] != 0:
        if m == len(food_times)-1:
            print(1)
        else:
            print(i+1)  
        
        break
        
    
              
              
                

    



