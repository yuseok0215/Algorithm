result = []
for i in range(1,10000):
    k = i

    num_1000 = i//1000 
    k %= 1000

    num_100 = k//100 
    k %= 100

    num_10 = k//10
    k %= 10

    num_1 = k
    result.append(i + num_1 + num_10 + num_100 + num_1000)


check_list = range(1,10001)

for i in check_list:
    if i not in result:
        print(i)
    
