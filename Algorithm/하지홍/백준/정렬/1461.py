n, m = map(int, input().split())

arr = list(map(int, input().split()))
    
minus_arr = []
plus_arr =[]
count = []
for elem in arr:
    if elem > 0:
        plus_arr.append(elem)
    else:
        minus_arr.append(elem)
        
minus_arr.sort(reverse=True)
plus_arr.sort(reverse=True)

for i in range(len(plus_arr)//m):
    count.append(plus_arr[i*m])
      
if len(plus_arr)%m >0:
    count.append(plus_arr[(len(plus_arr)//m)*m])
    
for i in range(len(minus_arr)//m):
    count.append(minus_arr[i*m])
if len(minus_arr)%m>0:
    count.append(minus_arr[(len(minus_arr)//m)*m])

count.sort(reverse=True)

if abs(count[0]) > abs(count[-1]):
    result = abs(count[0])
    for i in range(1,len(count)):
        result += 2*abs(count[i])
else:
    result = abs(count[-1])
    for i in range(len(count)-1):
        result += 2*abs(count[i])

print(result)


