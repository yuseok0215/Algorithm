N = int(input())

arr = list(map(int, str(N)))

length = len(arr)

first_sum = 0
second_sum = 0

for i in range(length//2):
    first_sum += arr[i]
    
for j in range(length//2, length):
    second_sum += arr[j]
    
if first_sum == second_sum:
    print("LUCKY")
else:
    print("READY")    