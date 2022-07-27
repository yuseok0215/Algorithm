food_times = [3, 1, 2]
k = 5
pointer = 0

answer = 0
while k != 0:
    for i in range(len(food_times)):
        if food_times[i] != 0:
            food_times[i] -= 1
            k -= 1
            pointer += 1
        else:
            pointer += 1
            
         
if pointer > len(food_times):
    pointer = pointer % len(food_times)
# print(pointer)
# ////////         
# ////////           
# if pointer > len(food_times):
#     pointer = pointer % len(food_times)

# for i in range(pointer, len(food_times)):
#     if food_times[i] != 0:
#         answer = i
#         break

# for elem in food_times:
#     if elem != 0:
#         continue
#     else:
#         print(1)
    
while True:
    if food_times[pointer] != 0:
        answer = pointer
        break
    pointer += 1

print(pointer+1)

        
        
