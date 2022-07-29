n = int(input())

zero, positive, negative = [], [], []

for _ in range(n):
    num = int(input())
    if num == 0:
        zero.append(num)
    elif num > 0:
        positive.append(num)
    else: 
        negative.append(num)
negative.sort()
positive.sort()
result = []

while negative:
    num1 = negative.pop(0)
    
    if negative:
        num2 = negative.pop(0)
        result.append(num1*num2)
    else:
        
        if zero:
            zero.pop()
        else:
            result.append(num1)
            
while positive:
    num1 = positive.pop()
    if num1 == 1:
        result.append(num1)
        continue
    # 양수 - 양수 짝이 있다면
    if positive:
        num2 = positive.pop()  
        if num2 == 1:
            result.append(num1)
            result.append(num2)
            continue
        result.append(num1*num2)
    else:
        result.append(num1)
print(sum(result))